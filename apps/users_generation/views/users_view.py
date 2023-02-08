from django.views.generic import TemplateView

from apps.users_generation.services.generate_users import generate_users


class UsersView(TemplateView):
    template_name = "users_generation/users.html"

    def get_context_data(self, count: int, **kwargs) -> dict:

        context_data = super().get_context_data(**kwargs)

        context_data["title"] = "Users"
        context_data["count"] = count

        context_data["users"] = generate_users(count=count)

        return context_data
