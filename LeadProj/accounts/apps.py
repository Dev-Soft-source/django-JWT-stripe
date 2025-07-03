from django.apps import AppConfig
import os


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        if os.environ.get('DJANGO_ENV') == 'development':
            from . import seed_users
            seed_users.create_seed_users()
