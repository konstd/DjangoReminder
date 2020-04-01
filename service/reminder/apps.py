from django.apps import AppConfig


class ReminderConfig(AppConfig):
    name = 'reminder'

    def ready(self):
        from reminder.signals import reminder  # noqa
