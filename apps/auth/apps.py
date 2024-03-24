from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .signal_receivers import send_sign_up_notification


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth'

    def ready(self) -> None:
        post_save.connect(send_sign_up_notification, sender=User)
