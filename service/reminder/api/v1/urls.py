from reminder.views.reminder import RemindersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    '',
    RemindersViewSet,
    basename='',
)

urlpatterns = [
] + router.urls
