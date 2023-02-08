from django.core.exceptions import ValidationError
from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.phone}"

    __repr__ = __str__

    def clean(self):
        if self.name.isdigit() or self.name is None:
            raise ValidationError("Enter right name!")
        if self.phone.isalpha() or self.phone is None:
            raise ValidationError("Enter right phone!")
        if not (self.phone.startswith("+380")):
            raise ValidationError("Phone must begin +380!")
