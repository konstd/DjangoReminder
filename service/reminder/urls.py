from django.urls import include, path

urlpatterns = [
    path('', include('reminder.api.v1.urls')),
]
