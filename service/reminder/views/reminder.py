from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from reminder.filters.reminder import ReminderFilter
from reminder.models import Reminder
from reminder.serializers.reminder import (ReminderSerializer,
                                           ReminderWriteSerializer)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class RemindersViewSet(ModelViewSet):

    serializer_class = ReminderSerializer
    permission_classes = (
        IsAuthenticated,
    )
    filter_backends = (
        DjangoFilterBackend,
    )
    filterset_class = ReminderFilter

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return ReminderWriteSerializer

        return ReminderSerializer

    def get_queryset(self):
        user = self.request.user

        return Reminder.objects\
            .select_related('owner')\
            .prefetch_related('participants')\
            .filter(
                Q(owner_id=user.id) | Q(participants__id=user.id)
            )\
            .distinct()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
