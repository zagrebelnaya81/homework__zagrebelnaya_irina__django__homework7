from django.urls import path, include


app_name = "users_generation"

urlpatterns = [
    path("users_generation/", include("apps.users_generation.urls", namespace="users_generation")),
    path("", include("apps.users_generation.urls_root")),
]
