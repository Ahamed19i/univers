# Generated by Django 5.0.4 on 2024-08-01 15:07

from django.db import migrations, models

"""
class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0017_administrateur_matricule_etudiant_matricule_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrateur',
            name='matricule',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='matricule',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='matricule',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]

"""


from django.db import migrations, models
import random

def generate_unique_matricule(apps, schema_editor):
    Etudiant = apps.get_model('site1', 'Etudiant')
    Professeur = apps.get_model('site1', 'Professeur')
    Administrateur = apps.get_model('site1', 'Administrateur')

    def get_unique_matricule():
        while True:
            matricule = random.randint(1000000000, 9999999999)  # Générer un matricule à 10 chiffres
            if not (Etudiant.objects.filter(matricule=matricule).exists() or 
                    Professeur.objects.filter(matricule=matricule).exists() or 
                    Administrateur.objects.filter(matricule=matricule).exists()):
                return matricule

    for etudiant in Etudiant.objects.all():
        etudiant.matricule = get_unique_matricule()
        etudiant.save(update_fields=['matricule'])

    for professeur in Professeur.objects.all():
        professeur.matricule = get_unique_matricule()
        professeur.save(update_fields=['matricule'])

    for administrateur in Administrateur.objects.all():
        administrateur.matricule = get_unique_matricule()
        administrateur.save(update_fields=['matricule'])

class Migration(migrations.Migration):

    dependencies = [
         # Remplacez par le nom de votre dernière migration
        ('site1', '0016_administrateur_photo_profil_etudiant_photo_profil_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='matricule',
            field=models.BigIntegerField(unique=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='professeur',
            name='matricule',
            field=models.BigIntegerField(unique=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='administrateur',
            name='matricule',
            field=models.BigIntegerField(unique=True, blank=True, null=True),
        ),
        migrations.RunPython(generate_unique_matricule),
        migrations.AlterField(
            model_name='etudiant',
            name='matricule',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='professeur',
            name='matricule',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='administrateur',
            name='matricule',
            field=models.BigIntegerField(unique=True),
        ),
    ]
