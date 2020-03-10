from api.views.doc_schema import schema_view
from django.urls import include, path

urlpatterns = [
    path('v1/', include('api.v1.urls')),

    path('docs/', schema_view.with_ui(cache_timeout=0), name="documentation")
]
