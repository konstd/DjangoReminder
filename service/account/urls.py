from django.urls import include, path

urlpatterns = [
    path('', include('account.api.v1.urls')),
]
