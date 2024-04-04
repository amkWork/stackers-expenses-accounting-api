from django.apps import AppConfig
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from .signal_receivers import send_sign_up_notification


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.auth'
    label = 'apps_auth'

    def ready(self) -> None:
        User = get_user_model()

        post_save.connect(send_sign_up_notification, sender=User)
