import logging

from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail

from reminder.models import Reminder

logger = logging.getLogger(__name__)


@shared_task
def send_email(reminder_id):
    try:
        reminder = Reminder.objects.select_related(
            'owner').prefetch_related('participants').get(pk=reminder_id)
    except Reminder.DoesNotExist:
        logger.warning(f"Reminder ({reminder_id}) does not exist.")
        return

    subject = f"Reminder: {reminder.title}"
    message = f"{reminder.body}. Location: {reminder.location}"

    recipients = list(reminder.participants.values_list("email", flat=True))
    recipients.append(reminder.owner.email)

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipients,
    )
