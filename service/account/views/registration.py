from account.serializers.account import AccountSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet


class CreateUserView(GenericViewSet, CreateModelMixin):

    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (
        permissions.AllowAny,
    )
