from django.urls import path, include

from apps.users_generation import views

app_name = "users_generation"
urlpatterns = [
    path(
        "users",
        include(
            [
                path("/<int:count>", views.UsersView.as_view(), name="with_args"),
            ]
        ),
    ),
    # path("<int:count>", "users/", views.UsersView.as_view(), name="users_generation"),
]
