from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/token/', obtain_auth_token, name='obtain_auth_token'),

    path('accounts/', include('account.urls')),
    path('reminders/', include('reminder.urls')),
]
