import random

from typing import NamedTuple
import string
from faker import Faker


class User(NamedTuple):
    login: str
    email: str
    password: str

    def __str__(self):
        return f"{self.login} {self.email}  {self.password}"

    __repr__ = __str__


faker = Faker()


def generate_user() -> User:
    name = faker.first_name() + "_" + faker.last_name()
    return User(
        login=name,
        email=name + "@gmail.com",
        password="".join([random.choice(string.ascii_letters + string.digits) for n in range(12)]),
    )


def generate_users(count: int = 10):
    for _ in range(count):
        yield generate_user()
