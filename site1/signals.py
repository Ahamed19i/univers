

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import EmploiDuTemps, Note, Absence, Notification

@receiver(post_save, sender=EmploiDuTemps)
def emploi_du_temps_updated(sender, instance, **kwargs):
    Notification.objects.create(
        user =instance.etudiant,
        message=f"L'emploi du temps a été mis à jour : {instance}",
    )
        
        
@receiver(post_save, sender=Note)
def note_updated(sender, instance, **kwargs):
    Notification.objects.create(
        user=instance.etudiant.user,
        message=f"Votre note a été mise à jour : {instance}",
    )


@receiver(post_save, sender=Absence)
def absence_updated(sender, instance, **kwargs):
    Notification.objects.create(
        user=instance.etudiant.user,
        message=f"Votre absence a été mise à jour : {instance}",
    )

"""@receiver(post_save, sender=Cours)
def cours_updated(sender, instance, **kwargs):
    students = instance.etudiants.all()
    for student in students:
        Notification.objects.create(
            user=student.user,
            message=f"Le cours {instance.nom_cours} a été mis à jour.",
        )
"""