from core import __version__
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Reminder API",
        default_version=__version__,
        description="Description",
        contact=openapi.Contact(
            name="Constantine Dementyev",
            email="co.de@outlook.com",
        ),
    ),
    public=True,
)
