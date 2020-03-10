from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as rest_filters
from reminder.models import Reminder


class ReminderFilter(rest_filters.FilterSet):

    owner = rest_filters.CharFilter(
        help_text=_('My reminders'),
        method='get_owner_reminders',
    )

    participant = rest_filters.CharFilter(
        help_text=_('Reminders where I participate'),
        method='get_participated_reminders',
    )

    class Meta:
        model = Reminder
        fields = (
            'owner',
            'participant',
        )

    def get_owner_reminders(self, queryset, name, value):
        if not value:
            return queryset

        return queryset.select_related('owner').filter(
            owner_id=self.request.user.id)

    def get_participated_reminders(self, queryset, name, value):
        if not value:
            return queryset

        return queryset.prefetch_related('participants').filter(
            participants__id=self.request.user.id)
