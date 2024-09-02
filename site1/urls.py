



from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, CustomLogoutView
#from .views import AbsenceListView, AbsenceCreateView, AbsenceUpdateView, AbsenceDeleteView
#from rest_framework.routers import DefaultRouter




urlpatterns = [

    
    path('', views.accueil, name='accueil'),
    
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    
    path('compte/', views.compte_utilisateur, name='compte_utilisateur'),
    
    path('etudiants/', views.etudiant_list, name='etudiant_list'),
    path('etudiant/<int:pk>/', views.etudiant_detail, name='etudiant_detail'),
    
    
    path('professeurs/', views.professeur_list, name='professeur_list'),
    path('professeurs/<int:pk>/', views.professeur_detail, name='professeur_detail'),
    
    
    #path('emploi_du_temps/', views.emploi_du_temps, name='emploi_du_temps'),
    
    #path('emploi_du_temps/', views.emploi_du_temps, name='emploi_du_temps'),
    
    path('emploi_du_temps/', views.emploi_du_temps, name='emploi_du_temps'),
    
    path('emploi_du_temps/pdf/', views.generate_pdf, name='generate_pdf'),
    
    
    #path('absences/', AbsenceListView.as_view(), name='absence-list'),
    #path('absences/new/', AbsenceCreateView.as_view(), name='absence-create'),
    #path('absences/<int:pk>/edit/', AbsenceUpdateView.as_view(), name='absence-update'),
    #path('absences/<int:pk>/delete/', AbsenceDeleteView.as_view(), name='absence-delete'),
    
    path('absences/', views.absences, name='absences'),
    path('absences/ajouter/', views.ajouter_absence, name='ajouter_absence'),
    path('modifier_absence/<int:absence_id>/', views.modifier_absence, name='modifier_absence'),
    path('supprimer_absence/<int:absence_id>/', views.supprimer_absence, name='supprimer_absence'),
    # Ajoutez d'autres URL si nécessaire
    #path('absences/etudiant/', views.absences_etudiant, name='absences_etudiant'),
    #path('reclamation/absence/<int:absence_id>/', views.reclamation_absence, name='reclamation_absence'),
    path('absence/etudiant/', views.absences_etudiant, name='absences_etudiant'),
    path('absences/justifier/<int:absence_id>/', views.justifier_absence, name='justifier_absence'),
    
    
    
    #path('', views.cours_list, name='cours_list'),
    #path('add/', views.cours_add, name='cours_add'),
    #path('<int:pk>/edit/', views.cours_edit, name='cours_edit'),
    #path('<int:pk>/delete/', views.cours_delete, name='cours_delete'),
    #path('<int:pk>/download/', views.cours_download, name='cours_download'),
    
    
    #path('cours/', views.cours_list, name='cours_list'),
    #path('cours/<int:pk>/', views.cours_detail, name='cours_detail'),
    #path('cours/<int:pk>/', views.cours_edit, name='cours_edit'),
    
    #path('cours/', views.cours_list, name='cours_list'),
    #path('cours/add/', views.cours_add, name='cours_add'),
    #path('cours/<int:pk>/edit/', views.cours_edit, name='cours_edit'),
    #path('cours/<int:pk>/delete/', views.cours_delete, name='cours_delete'),
    #path('cours/<int:pk>/download/', views.cours_download, name='cours_download'),
    
    path('cours/', views.cours_list, name='cours_list'),
    path('cours/etudiant/', views.cours_list_etudiant, name='cours_list_etudiant'),
    path('cours/add/', views.cours_add, name='cours_add'),
    path('cours/<int:pk>/edit/', views.cours_edit, name='cours_edit'),
    path('cours/<int:pk>/delete/', views.cours_delete, name='cours_delete'),
    path('cours/<int:pk>/download/', views.cours_download, name='cours_download'),
    
    
    
    path('', views.actualites_list, name='actualites_list'),
    path('<int:pk>/', views.actualite_detail, name='actualite_detail'),
    
    
    path('photos/', views.photos_list, name='photos_list'),
    
    
    #path('notes/etudiant/', views.notes_etudiant, name='notes_etudiant'),
    # path('notes_professeur/', views.notes_professeur, name='notes_professeur'),
    # path('modifier_note/<int:note_pk>/', views.modifier_note, name='modifier_note'),
    # path('supprimer_note/<int:note_pk>/', views.supprimer_note, name='supprimer_note'),
    #path('notes/reclamation/<int:note_id>/', views.note_reclamation, name='note_reclamation'),
    # path('notes/ajouter/', views.ajouter_note, name='ajouter_note'),
    #path('notes/reclamation/<int:note_id>/', views.note_reclamation, name='note_reclamation'),
    
    
    path('notes_professeur/', views.notes_professeur, name='notes_professeur'),
    path('notes_etudiant/', views.notes_etudiant, name='notes_etudiant'),
    path('notes/ajouter/', views.ajouter_note, name='ajouter_note'),
    #path('ajouter_note/', views.ajouter_note, name='ajouter_note'),
    path('modifier_note/<int:note_id>/', views.modifier_note, name='modifier_note'),
    path('supprimer_note/<int:note_id>/', views.supprimer_note, name='supprimer_note'),
    path('note_reclamation/<int:note_id>/', views.note_reclamation, name='note_reclamation'),
    path('reclamation/traiter/<int:reclamation_id>/', views.traiter_reclamation, name='traiter_reclamation'),
    #path('traiter_reclamation/<int:reclamation_id>/', views.traiter_reclamation, name='traiter_reclamation'),
    
    
    path('notes/', views.notes_etudiant, name='notes_etudiant'),
    path('notes/reclamer/<int:note_id>/', views.note_reclamation, name='note_reclamation'),
    
    
    path('notifications/', views.notifications, name='notifications'),
    #path('documents-recents/', views.documents_recents, name='documents_recents'),
]

