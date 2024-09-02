from django.apps import AppConfig


class Site1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site1'
    
    def ready(self):
        import site1.signals



