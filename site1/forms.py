

from django import forms
from .models import Etudiant, Professeur, Cours


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'date_naissance', 'adresse', 'email', 'telephone', 'departement', 'filiere', 'niveau']

# le formulaire professeurs
class ProfesseurForm(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = ['nom', 'prenom', 'email', 'telephone', 'departement']
    
    

# Formulaire pour cours

from django import forms
from .models import Cours

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['nom_cours', 'description', 'credits', 'coefficient', 'filieres', 'fichier_pdf']

    def clean_fichier_pdf(self):
        fichier = self.cleaned_data.get('fichier_pdf')
        if fichier:
            if not fichier.name.endswith('.pdf'):
                raise forms.ValidationError('Le fichier doit être au format PDF.')
        return fichier






# Formulaire Actualités

from .models import Actualite

class ActualiteForm(forms.ModelForm):
    class Meta:
        model = Actualite
        fields = ['titre', 'description', 'image']


from django import forms
from .models import Reclamation, Note

class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ['note', 'etudiant', 'motif', 'statut']
        
        

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['etudiant', 'cours', 'note', 'date']
        


from django import forms
from .models import Absence

class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['etudiant', 'cours', 'date', 'justifiee']



from django import forms
from .models import Justifier

class JustifierForm(forms.ModelForm):
    class Meta:
        model = Justifier
        fields = ['motif']
