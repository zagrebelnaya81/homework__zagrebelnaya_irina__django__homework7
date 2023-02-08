from django.urls import path, include


urlpatterns = [
    path("users_generation/", include("apps.users_generation.urls", namespace="users_generation")),
    path("", include("apps.users_generation.urls_root")),
    path("contacts/", include("apps.contacts.urls")),
]
