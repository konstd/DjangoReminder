from django.db.models.signals import (
    post_save,
    pre_delete,
)
from django.dispatch import receiver

from celery.result import AsyncResult
from reminder.models import Reminder

from core.tasks import send_email


@receiver(post_save, sender=Reminder)
def create_update_reminder(sender, instance, created, **kwargs) -> None:
    """
    Create or update reminder.

    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return: None
    """

    if not created and instance.celery_task_id:
        AsyncResult(instance.celery_task_id).revoke()

    if instance.completed:
        return

    task_id = send_email.apply_async(
        (
            instance.id,
        ),
        eta=instance.target_date,
    ).id

    Reminder.objects \
        .filter(id=instance.id) \
        .update(celery_task_id=task_id)


@receiver(pre_delete, sender=Reminder)
def delete_reminder(sender, instance, **kwargs) -> None:
    """
    Delete reminder.

    :param sender:
    :param instance:
    :param kwargs:
    :return: None
    """
    if instance.celery_task_id:
        AsyncResult(instance.celery_task_id).revoke()
