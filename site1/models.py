



import random
from django.db import models
from django.contrib.auth.models import User
import uuid

class Departement(models.Model):
    nom_departement = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_departement

class Filiere(models.Model):
    nom_filiere = models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='filieres')

    def __str__(self):
        return self.nom_filiere

class Niveau(models.Model):
    nom_niveau = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_niveau

class Salle(models.Model):
    nom_salle = models.CharField(max_length=100)
    capacite = models.IntegerField()
    localisation = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_salle

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='etudiant')
    matricule = models.BigIntegerField(unique=True, blank=True, null=True)
    #matricule = models.CharField(max_length=100, unique=True, blank=True, null=True)  # Temporairement autorisé à être vide
    #matricule = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    
    date_naissance = models.DateField(null=True, blank=True)
    lieu_naissance = models.CharField(max_length=100, null=True, blank=True)
    situation_familiale = models.CharField(max_length=100, null=True, blank=True)
    nationalite = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)  
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='etudiants')
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, related_name='etudiants')
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, related_name='etudiants')
    photo_profil = models.ImageField(upload_to='photos_profil/', default='photos_profil/default_etudiant.jpg')
    
    
    def generate_unique_matricule(self):
        while True:
        # Générer un matricule aléatoire dans une plage spécifiée
            matricule = random.randint(1000000000, 9999999999)  # 10 chiffres
            if not Administrateur.objects.filter(matricule=matricule).exists():
                return matricule

    def save(self, *args, **kwargs):
        if self.matricule is None:
            self.matricule = self.generate_unique_matricule()
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f'{self.nom} {self.prenom} ({self.matricule})'   
    
    def calculer_moyenne(self):
        inscriptions = Inscription.objects.filter(etudiant=self)
        total_points = 0
        total_credits = 0

        for inscription in inscriptions:
            notes = Note.objects.filter(etudiant=self, cours=inscription.cours)
            for note in notes:
                cours = note.cours
                total_points += note.note * cours.coefficient * cours.credits
                total_credits += cours.credits

        if total_credits > 0:
            moyenne = total_points / total_credits
        else:
            moyenne = 0

        return moyenne

class Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professeur')
    matricule = models.BigIntegerField(unique=True, blank=True, null=True)
    #matricule = models.CharField(max_length=100, unique=True, blank=True, null=True)  # Temporairement autorisé à être vide
    #matricule = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    
    date_naissance = models.DateField(null=True, blank=True)
    lieu_naissance = models.CharField(max_length=100, null=True, blank=True)
    situation_familiale = models.CharField(max_length=100, null=True, blank=True)
    nationalite = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length=255, default='Adresse non fournie')
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='professeurs')
    photo_profil = models.ImageField(upload_to='photos_profil/', default='photos_profil/default_professeur.jpg')
    
   
    def generate_unique_matricule(self):
            while True:
            # Générer un matricule aléatoire dans une plage spécifiée
                matricule = random.randint(1000000000, 9999999999)  # 10 chiffres
                if not Administrateur.objects.filter(matricule=matricule).exists():
                    return matricule

    def save(self, *args, **kwargs):
        if self.matricule is None:
            self.matricule = self.generate_unique_matricule()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.nom} {self.prenom} ({self.matricule})'
   
    

class Administrateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrateur')
    matricule = models.BigIntegerField(unique=True, blank=True, null=True)
    #matricule = models.CharField(max_length=100, unique=True, blank=True, null=True)  # Temporairement autorisé à être vide
    #matricule = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    
    date_naissance = models.DateField(null=True, blank=True)
    lieu_naissance = models.CharField(max_length=100, null=True, blank=True)
    situation_familiale = models.CharField(max_length=100, null=True, blank=True)
    nationalite = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length=255, default='Adresse non fournie')
    telephone = models.CharField(max_length=15, default='trlrphone non fournie')
    email = models.EmailField()
    
    photo_profil = models.ImageField(upload_to='photos_profil/', default='photos_profil/default_administrateur.jpg')
    
    def generate_unique_matricule(self):
        while True:
        # Générer un matricule aléatoire dans une plage spécifiée
            matricule = random.randint(1000000000, 9999999999)  # 10 chiffres
            if not Administrateur.objects.filter(matricule=matricule).exists():
                return matricule

    def save(self, *args, **kwargs):
        if self.matricule is None:
            self.matricule = self.generate_unique_matricule()
        super().save(*args, **kwargs)
    
        
    def __str__(self):
        return f'{self.nom} {self.prenom} ({self.matricule})'
    
        

class Cours(models.Model):
    nom_cours = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.IntegerField()
    coefficient = models.FloatField()
    filieres = models.ForeignKey(Filiere, on_delete=models.CASCADE, related_name='cours' )
    fichier_pdf = models.FileField(upload_to='cours_pdfs/', default='cours_pdfs/default.pdf')

    def __str__(self):
        return self.nom_cours

class CoursProfesseur(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='cours_professeurs')
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE, related_name='cours_professeurs')

    class Meta:
        unique_together = (('cours', 'professeur'),)

    def __str__(self):
        return f'{self.cours.nom_cours} - {self.professeur.nom}'

class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='notes')
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='notes')
    note = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f'{self.etudiant.nom} {self.etudiant.prenom} - {self.cours.nom_cours}: {self.note}'

class EmploiDuTemps(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='emplois_du_temps', default=1) 
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='emplois_du_temps')
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE, related_name='emplois_du_temps')
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, related_name='emplois_du_temps')
    jour = models.CharField(max_length=10)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def __str__(self):
        return f'{self.cours.nom_cours} - {self.jour} {self.heure_debut}-{self.heure_fin}'
    
    

class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='absences')
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='absences')
    date = models.DateField()
    justifiee = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.etudiant.nom} {self.etudiant.prenom} - {self.cours.nom_cours} : {self.date}'


class Inscription(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='inscriptions')
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='inscriptions')
    date_inscription = models.DateField()

    def __str__(self):
        return f'{self.etudiant.nom} {self.etudiant.prenom} - {self.cours.nom_cours} : {self.date_inscription}'


class MoyennePonderee(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='moyennes_ponderees')
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, related_name='moyennes_ponderees')
    moyenne = models.FloatField(default=0.0)

    def __str__(self):
        return f'Moyenne de {self.etudiant.nom} {self.etudiant.prenom} : {self.moyenne}'

    def save(self, *args, **kwargs):
        self.moyenne = self.etudiant.calculer_moyenne()
        super().save(*args, **kwargs)

class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='actualites/')

    def __str__(self):
        return self.titre



class Photo(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.titre



class ImportantNote(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
    
 

class RecentDocument(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50)
    fichier = models.FileField(upload_to='documents_recents/')
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.etudiant.nom} {self.etudiant.prenom} - {self.document_type}'
    


class Reclamation(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='reclamations')
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='reclamations')
    motif = models.TextField()
    date = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=10, choices=[('En cours', 'En cours'), ('Traitée', 'Traitée')], default='En cours')

    def __str__(self):
        return f'Reclamation by {self.etudiant.nom} {self.etudiant.prenom} for {self.note.cours.nom_cours}'



class Justifier(models.Model):
    absence = models.ForeignKey('Absence', on_delete=models.CASCADE, related_name='justifier')
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE, related_name='justifier')
    motif = models.TextField()
    date_justification = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=10, choices=[('En cours', 'En cours'), ('Traitée', 'Traitée'), ('Refusée', 'Refusée')], default='En cours')
    #statut = models.CharField(max_length=10, choices=[('En cours', 'En cours'), ('Traitée', 'Traitée')], default='En cours')

    def __str__(self):
        return f'{self.etudiant.nom} {self.etudiant.prenom} - {self.absence.cours.nom_cours} : {self.date_justification}'




class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user.username} - {self.message[:20]}'