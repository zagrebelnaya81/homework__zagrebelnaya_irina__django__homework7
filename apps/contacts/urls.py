from django.urls import path, include

from . import views

app_name = "contacts"

urlpatterns = [
    path(
        "list/",
        include(
            [
                path("contacts/", views.ContactsListView.as_view(), name="list"),
            ]
        ),
    ),
    path("create/", views.ContactsCreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.ContactsUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.ContactsDeleteView.as_view(), name="delete"),
]
