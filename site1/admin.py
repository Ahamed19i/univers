

from django.contrib import admin
from .models import (
    Departement, Filiere, Niveau, Salle, Etudiant, Professeur, 
    Cours, CoursProfesseur, Note, EmploiDuTemps, Inscription, 
    MoyennePonderee, Actualite, Photo, ImportantNote, RecentDocument, 
    Reclamation, Administrateur, Notification
)


class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image', 'date_publication')
    


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('titre',  'description', 'image', 'date_publication')
    

class ImportantNoteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'date_publication') 


class RecentDocumentAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'document_type', 'fichier', 'date_ajout', )


class ReclamationAdmin(admin.ModelAdmin):
    list_display = ('note', 'etudiant', 'motif', 'date', 'statut')
    

class DepartementAdmin(admin.ModelAdmin):
    list_display = ('nom_departement',)

class FiliereAdmin(admin.ModelAdmin):
    list_display = ('nom_filiere', 'departement')

class NiveauAdmin(admin.ModelAdmin):
    list_display = ('nom_niveau',)

class SalleAdmin(admin.ModelAdmin):
    list_display = ('nom_salle', 'capacite', 'localisation')

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'date_naissance', 'adresse', 'email', 'telephone', 'departement', 'filiere', 'niveau')
    search_fields = ('nom', 'prenom', 'email')
    list_filter = ('departement', 'filiere', 'niveau')
    

class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'telephone', 'departement')
    search_fields = ('nom', 'prenom', 'email')
    list_filter = ('departement',)
    

# Administrateur

class AdministrateurAdimn(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')
    

class CoursAdmin(admin.ModelAdmin):
    list_display = ('nom_cours', 'description', 'credits', 'coefficient')
    search_fields = ('nom_cours',)
    list_filter = ('filieres',)
     

class CoursProfesseurAdmin(admin.ModelAdmin):
    list_display = ('cours', 'professeur')
    search_fields = ('cours__nom_cours', 'professeur__nom')
    list_filter = ('cours', 'professeur')
    
    

class NoteAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'cours', 'note', 'date')
    search_fields = ('etudiant__nom', 'cours__nom_cours')
    list_filter = ('cours', 'date')
    
    

class EmploiDuTempsAdmin(admin.ModelAdmin):
    list_display = ('cours', 'professeur', 'salle', 'jour', 'heure_debut', 'heure_fin')
    search_fields = ('cours__nom_cours', 'professeur__nom', 'salle__nom_salle')
    list_filter = ('jour', 'salle')




class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'cours', 'date_inscription')
    search_fields = ('etudiant__nom', 'cours__nom_cours')
    list_filter = ('cours', 'date_inscription')



class RoleAdmin(admin.ModelAdmin):
    list_display = ('nom_role', 'description_role')

class MoyennePondereeAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'filiere', 'moyenne')
    search_fields = ('etudiant__nom', 'filiere__nom_filiere')
    list_filter = ('filiere',)
    




from .models import Absence, Justifier

@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'cours', 'date', 'justifiee')
    list_filter = ('etudiant', 'cours', 'date', 'justifiee')
    search_fields = ('etudiant__nom', 'etudiant__prenom', 'cours__nom_cours')
    ordering = ('-date',)

@admin.register(Justifier)
class JustifierAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'absence', 'motif', 'date_justification', 'statut')
    list_filter = ('statut', 'date_justification', 'absence__cours', 'etudiant')
    search_fields = ('etudiant__nom', 'etudiant__prenom', 'absence__cours__nom_cours', 'motif')
    ordering = ('-date_justification',)
    actions = ['accepter_justification', 'refuser_justification']

    def accepter_justification(self, request, queryset):
        queryset.update(statut='Acceptée')
        for justification in queryset:
            justification.absence.justifiee = True
            justification.absence.save()
        self.message_user(request, "Les justifications sélectionnées ont été acceptées.")

    accepter_justification.short_description = "Accepter les justifications sélectionnées"

    def refuser_justification(self, request, queryset):
        queryset.update(statut='Refusée')
        self.message_user(request, "Les justifications sélectionnées ont été refusées.")

    refuser_justification.short_description = "Refuser les justifications sélectionnées"


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read')














admin.site.register(Actualite, ActualiteAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(ImportantNote, ImportantNoteAdmin)
admin.site.register(RecentDocument, RecentDocumentAdmin)
admin.site.register(Reclamation, ReclamationAdmin)
admin.site.register(Notification, NotificationAdmin)


admin.site.register(Departement, DepartementAdmin)
admin.site.register(Filiere, FiliereAdmin)
admin.site.register(Niveau, NiveauAdmin)
admin.site.register(Salle, SalleAdmin)
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Professeur, ProfesseurAdmin)
admin.site.register(Cours, CoursAdmin)
admin.site.register(CoursProfesseur, CoursProfesseurAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(EmploiDuTemps, EmploiDuTempsAdmin)
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(MoyennePonderee, MoyennePondereeAdmin)
admin.site.register(Administrateur, AdministrateurAdimn)


