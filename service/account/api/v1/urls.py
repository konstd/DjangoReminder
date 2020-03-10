from account.views.account import AccountList, SessionAccount
from account.views.registration import CreateUserView
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    'registration',
    CreateUserView,
)

router.register(
    '',
    AccountList,
    basename=''
)

urlpatterns = [
    path('me/', SessionAccount.as_view(), name='session_profile'),
] + router.urls
