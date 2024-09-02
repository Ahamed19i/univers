
# La vue du page d'accueil du plateforme

from django.shortcuts import render, get_object_or_404, redirect
from .models import Etudiant, Professeur, EmploiDuTemps, ImportantNote, Absence, RecentDocument
  

    
    
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ImportantNote, Photo, Absence

from .models import Notification

"""@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'site1/notifications.html', {'notifications': notifications})"""


@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    print(f'Notifications for {request.user.username}: {notifications}')  # Vérifiez les notifications dans la console
    notifications.update(is_read=True)  # Marquer les notifications comme lues
    return render(request, 'site1/notifications.html', {'notifications': notifications})


@login_required
def accueil(request):
    user = request.user
    photos = Photo.objects.all()
    notes_importantes = ImportantNote.objects.all()
    notifications_non_lues = Notification.objects.filter(user=request.user, is_read=False).count()
    
    # Afficher les absences uniquement si l'utilisateur est un étudiant
    if hasattr(user, 'etudiant'):
        absences = Absence.objects.filter(etudiant=user.etudiant)
    else:
        absences = []

    return render(request, 'site1/accueil.html', {
        'photos': photos,
        'notes_importantes': notes_importantes,
        'absences': absences,
        'notifications_non_lues': notifications_non_lues,
    })

#Le views pour le login et logout
# Ici La classe CustomLoginView hérite de LoginView, 
# une vue générique intégrée de Django utilisée pour gérer les connexions des utilisateurs.
# Par la suite on pourrais bien personnaliser cette vue qui permettra d'adapter
# l'expérience utilisateur aux besoins spécifiques de votre application 



# La vue Etudiant en general
def etudiant_list(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'site1/etudiant_list.html', {'etudiants': etudiants})

def etudiant_detail(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    return render(request, 'site1/etudiant_detail.html', {'etudiant': etudiant})


    

# La vue professeur en general
def professeur_list(request):
    professeurs = Professeur.objects.all()
    return render(request, 'site1/professeur_list.html', {'professeurs': professeurs})

def professeur_detail(request, pk):
    professeur = get_object_or_404(Professeur, pk=pk)
    return render(request, 'site1/professeur_detail.html', {'professeur': professeur})



#def emploi_du_temps(request):

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EmploiDuTemps, Absence, Etudiant, Cours, Professeur
from .forms import AbsenceForm

@login_required
def emploi_du_temps(request):
    emploi_du_temps_list = EmploiDuTemps.objects.all()
    absences = Absence.objects.all()

    if request.method == 'POST':
        absence_form = AbsenceForm(request.POST)
        if absence_form.is_valid():
            absence_form.save()
            return redirect('emploi_du_temps')
    else:
        absence_form = AbsenceForm()

    context = {
        'emploi_du_temps_list': emploi_du_temps_list,
        'absences': absences,
        'absence_form': absence_form,
    }
    return render(request, 'site1/emploi_du_temps.html', context)





#La partie Absence pour les etudiants

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Absence, Justifier
from .forms import ReclamationForm, JustifierForm

@login_required
def absences_etudiant(request):
    absences_list = Absence.objects.filter(etudiant=request.user.etudiant)

    context = {
        'absences_list': absences_list,
    }
    return render(request, 'site1/absences_etudiant.html', context)

@login_required
def justifier_absence(request, absence_id):
    absence = get_object_or_404(Absence, id=absence_id)
    if request.method == 'POST':
        form = JustifierForm(request.POST)
        if form.is_valid():
            justification = form.save(commit=False)
            justification.absence = absence
            justification.etudiant = request.user.etudiant
            justification.save()
            return redirect('absences_etudiant')
    else:
        form = JustifierForm()

    context = {
        'absence': absence,
        'form': form,
    }
    return render(request, 'site1/justifier_absence.html', context)


@login_required
def gerer_justifications(request):
    if not request.user.is_staff:  # Assuming admin users have is_staff=True
        return redirect('absences_etudiant')
    
    justifications = Justifier.objects.filter(statut='En cours')
    if request.method == 'POST':
        justification_id = request.POST.get('justification_id')
        action = request.POST.get('action')
        justification = get_object_or_404(Justifier, id=justification_id)
        if action == 'accepter':
            justification.statut = 'Acceptée'
        elif action == 'refuser':
            justification.statut = 'Refusée'
        justification.save()
        return redirect('gerer_justifications')

    context = {
        'justifications': justifications,
    }
    return render(request, 'site1/gerer_justifications.html', context)




# Pour gerer les absences by Admin and Professeur

@login_required
def absences(request):
    absences_list = Absence.objects.all()

    if request.method == 'POST':
        absence_form = AbsenceForm(request.POST)
        if absence_form.is_valid():
            absence_form.save()
            return redirect('absences')
    else:
        absence_form = AbsenceForm()

    context = {
        'absences_list': absences_list,
        'absence_form': absence_form,
    }
    return render(request, 'site1/absences.html', context)


@login_required
def modifier_absence(request, absence_id):
    absence = get_object_or_404(Absence, id=absence_id)
    if request.method == 'POST':
        form = AbsenceForm(request.POST, instance=absence)
        if form.is_valid():
            form.save()
            return redirect('absences')
    else:
        form = AbsenceForm(instance=absence)

    return render(request, 'site1/modifier_absence.html', {'form': form})





@login_required
def supprimer_absence(request, absence_id):
    absence = get_object_or_404(Absence, id=absence_id)
    if request.method == 'POST':
        absence.delete()
        return redirect('absences')

    return render(request, 'site1/supprimer_absence.html', {'absence': absence})  



@login_required
def ajouter_absence(request):
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('absences')
    else:
        form = AbsenceForm()

    return render(request, 'site1/ajouter_absence.html', {'form': form})





# views pour regener un pdf et le telecharger
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from .models import EmploiDuTemps

def generate_pdf(request):
    # Crée une réponse HTTP avec un type de contenu PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="emploi_du_temps.pdf"'

    # Crée un document ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)
    elements = []

    # Récupère les données de l'emploi du temps
    emploi_du_temps_list = EmploiDuTemps.objects.all()

    # Définir les données du tableau
    data = [["Jour", "Cours", "Professeur", "Salle", "Heure de Début", "Heure de Fin"]]

    for emploi in emploi_du_temps_list:
        data.append([
            emploi.jour,
            emploi.cours.nom_cours,
            emploi.professeur.nom,
            emploi.salle.nom_salle,
            emploi.heure_debut.strftime("%H:%M"),
            emploi.heure_fin.strftime("%H:%M")
        ])

    # Crée un tableau avec les données
    table = Table(data)

    # Définir les styles du tableau
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    # Ajouter le tableau aux éléments
    elements.append(table)

    # Construit le document PDF
    doc.build(elements)

    return response



# Views pour les actions des cours 

# Processus d'authentification du Prof et Admin
# Puis processus CRUD du module cours

# Processus d'authentification du Prof et Admin

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse
from .models import Cours
from .forms import CoursForm

def est_administrateur_ou_professeur(user):
    return user.is_authenticated and (user.is_staff or user.groups.filter(name='Professeurs').exists())

def cours_list(request):
    cours = Cours.objects.all()
    est_admin_ou_prof = request.user.is_authenticated and (request.user.is_staff or request.user.groups.filter(name='Professeurs').exists())
    return render(request, 'site1/cours_list.html', {'cours': cours, 'est_admin_ou_prof': est_admin_ou_prof})

@login_required
@user_passes_test(est_administrateur_ou_professeur)
def cours_add(request):
    if request.method == 'POST':
        form = CoursForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cours_list')
    else:
        form = CoursForm()
    return render(request, 'site1/cours_add.html', {'form': form})

@login_required
@user_passes_test(est_administrateur_ou_professeur)
def cours_edit(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        form = CoursForm(request.POST, request.FILES, instance=cours)
        if form.is_valid():
            form.save()
            return redirect('cours_list')
    else:
        form = CoursForm(instance=cours)
    return render(request, 'site1/cours_edit.html', {'form': form})

@login_required
@user_passes_test(est_administrateur_ou_professeur)
def cours_delete(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        cours.delete()
        return redirect('cours_list')
    return render(request, 'site1/cours_confirm_delete.html', {'cours': cours})

def cours_download(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    response = FileResponse(cours.fichier_pdf.open(), as_attachment=True)
    return response




#Etudiant cours, consult et telecharge

def cours_list_etudiant(request):
    cours = Cours.objects.all()
    return render(request, 'site1/cours_list_etudiant.html', {'cours': cours})





# Views Actualités
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Actualite
from .forms import ActualiteForm

def actualites_list(request):
    actualites = Actualite.objects.all().order_by('-date_publication')
    return render(request, 'site1/actualites_list.html', {'actualites': actualites})

def actualite_detail(request, pk):
    actualite = get_object_or_404(Actualite, pk=pk)
    return render(request, 'site1/actualite_detail.html', {'actualite': actualite})



# la gelleries photos
from django.shortcuts import render
from .models import Photo

def photos_list(request):
    photos = Photo.objects.all().order_by('-date_publication')
    return render(request, 'site1/photos_list.html', {'photos': photos})



# compte utilisateur

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Etudiant, Professeur, Administrateur

@login_required
def compte_utilisateur(request):
    etudiant = None
    professeur = None
    administrateur = None

    if hasattr(request.user, 'etudiant'):
        etudiant = request.user.etudiant
    elif hasattr(request.user, 'professeur'):
        professeur = request.user.professeur
    elif hasattr(request.user, 'administrateur'):
        administrateur = request.user.administrateur

    return render(request, 'compte_utilisateur.html', {
        'etudiant': etudiant,
        'professeur': professeur,
        'administrateur': administrateur
    })









# toujours sur login

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redirige les utilisateurs authentifiés
    next_page = reverse_lazy('accueil')  # Redirige après la connexion

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirige après la déconnexion




# Views pour la note et la moyenne de l'etudiant

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note, Etudiant, Professeur, Reclamation, CoursProfesseur
from .forms import ReclamationForm, NoteForm


@login_required
def notes_professeur(request):
    professeur = Professeur.objects.get(user=request.user)
    cours_professeur = Cours.objects.filter(cours_professeurs__professeur=professeur)
    notes = Note.objects.filter(cours__in=cours_professeur).prefetch_related('reclamations')

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_professeur')
    else:
        form = NoteForm()

    context = {
        'form': form,
        'notes': notes,
    }
    return render(request, 'site1/notes_professeur.html', context)




@login_required
def modifier_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_professeur')
    else:
        form = NoteForm(instance=note)

    return render(request, 'site1/modifier_note.html', {'form': form})


@login_required
def supprimer_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_professeur')

    return render(request, 'site1/supprimer_note.html', {'note': note})

@login_required
def notes_etudiant(request):
    etudiant = get_object_or_404(Etudiant, user=request.user)
    notes = Note.objects.filter(etudiant=etudiant).prefetch_related('reclamations')
    return render(request, 'site1/notes_etudiant.html', {'notes': notes})


@login_required
def note_reclamation(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        motif = request.POST.get('motif', '')
        Reclamation.objects.create(note=note, etudiant=note.etudiant, motif=motif)
        return redirect('notes_etudiant')
    return render(request, 'site1/note_reclamation.html', {'note': note})


@login_required
def ajouter_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_professeur')
    else:
        form = NoteForm()

    return render(request, 'site1/ajouter_note.html', {'form': form})



@login_required
def traiter_reclamation(request, reclamation_id):
    reclamation = get_object_or_404(Reclamation, pk=reclamation_id)

    if request.method == 'POST':
        reclamation.statut = request.POST.get('statut', 'En cours')
        reclamation.save()
        return redirect('notes_professeur')

    context = {
        'reclamation': reclamation,
    }
    return render(request, 'site1/traiter_reclamation.html', context)


