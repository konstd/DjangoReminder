from account.permissions import AccountPermission
from account.serializers.account import AccountSerializer
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet


class AccountList(ReadOnlyModelViewSet):

    serializer_class = AccountSerializer
    permission_classes = (
        IsAuthenticated,
        AccountPermission,
    )

    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)


class SessionAccount(RetrieveUpdateAPIView):

    queryset = User
    serializer_class = AccountSerializer
    permission_classes = (
        IsAuthenticated,
        AccountPermission,
    )

    def get_object(self):
        return self.request.user
