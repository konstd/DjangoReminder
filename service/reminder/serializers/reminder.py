from datetime import datetime

from account.serializers.account import AccountSerializer
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from reminder.models import Reminder
from rest_framework import serializers


class ReminderSerializer(serializers.ModelSerializer):

    owner = AccountSerializer()
    participants = AccountSerializer(many=True)

    class Meta:
        model = Reminder
        fields = (
            'id',
            'owner',
            'title',
            'body',
            'location',
            'participants',
            'created_at',
            'target_date',
            'completed',
        )
        extra_kwargs = {
            'id': {
                'read_only': True,
            },
            'owner': {
                'read_only': True,
            }
        }

    def validate_target_date(self, date):
        now = datetime.now(tz=timezone.utc)
        if now <= date:
            return date

        raise serializers.ValidationError(
            _('Error. Chosen date is earlier than current date'),
        )


class ReminderWriteSerializer(ReminderSerializer):

    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    participants = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all())
