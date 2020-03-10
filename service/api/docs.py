from drf_yasg import openapi
from drf_yasg.inspectors import PaginatorInspector


class ReminderPaginatorInspector(PaginatorInspector):

    def get_paginator_parameters(self, paginator):
        return [
            openapi.Parameter(
                name="page_size",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Number of items per page",
                default=10,
            ),
            openapi.Parameter(
                name="page",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number",
                default=1,
            ),
        ]

    def get_paginated_response(self, paginator, response_schema):
        return response_schema
