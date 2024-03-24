from typing import Any

from django.contrib.auth.models import User
from django.core.mail import send_mail


def send_sign_up_notification(
    sender: type[User],
    instance: User,
    created: bool,
    **kwargs: Any,
) -> None:
    if created:
        send_mail(
            subject='New User Created',
            message=(
                f'New user was created, using your email `{instance.email}`!\n'
                '\n'
                'Auto-generated message from StackersExpensesAccountingApp.'
            ),
            from_email='noreply@example.com',
            recipient_list=[
                instance.email,
            ],
            fail_silently=False,
        )
