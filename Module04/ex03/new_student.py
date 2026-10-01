import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Validate name and surname, then build the login and id."""
        if not isinstance(self.name, str) or not isinstance(self.surname, str):
            raise TypeError("name and surname must be strings")
        if not self.name or not self.surname:
            raise ValueError("name and surname must not be empty")
        self.login = self.name[0] + self.surname
        self.id = generate_id()
