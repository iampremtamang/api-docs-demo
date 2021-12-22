from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Todo Api',
        default_version='v1',
        description='Swagger documentation for ToDo Apis',
        terms_of_service='ttps://www.google.com/policies/terms/"',
        contact=openapi.Contact(email='ktamangprem@gmail.com'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/todo/', include("todos.urls")),
    path('docs/', include_docs_urls('Todo Api')),
    path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
