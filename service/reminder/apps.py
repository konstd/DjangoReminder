from django.apps import AppConfig


class ReminderConfig(AppConfig):
    name = 'reminder'

    def ready(self):
        import reminder.signals.reminder  # noqa
