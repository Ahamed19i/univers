


from django_cron import CronJobBase, Schedule
from datetime import timedelta
from django.utils import timezone
from .models import Notification

class CleanUpNotificationsJob(CronJobBase):
    RUN_EVERY_MINS = 60  # Exécuter toutes les heures

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'site1.clean_up_notifications'  # Un code unique pour identifier ce job

    def do(self):
        cutoff = timezone.now() - timedelta(hours=48)
        Notification.objects.filter(is_read=True, timestamp__lt=cutoff).delete()
