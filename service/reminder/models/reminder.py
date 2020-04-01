import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Reminder(models.Model):
    """ Reminder model """

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='reminders',
        verbose_name=_('Owner'),
    )

    title = models.CharField(
        max_length=255,
        verbose_name=_('Title'),
    )

    body = models.TextField(
        verbose_name=_('Body'),
    )

    location = models.CharField(
        max_length=255,
        verbose_name=_('Location'),
    )

    participants = models.ManyToManyField(
        User,
        blank=True,
        related_name='reminder_participants',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    target_date = models.DateTimeField(
        verbose_name=_('Target date'),
    )

    completed = models.BooleanField(
        default=False,
    )

    celery_task_id = models.CharField(
        max_length=255,
        blank=True,
    )

    def __str__(self):
        return f"{self.owner.email} {self.title}"

    class Meta:
        app_label = 'reminder'
