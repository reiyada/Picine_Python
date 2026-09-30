from S1E9 import Character


class Baratheon(Character):
    """This is a child class of Character, and this has
        family_name, eyes, and hairs as its unique properties."""

    def __init__(self, first_name: str,
                 is_alive: bool = True,
                 family_name: str = "Baratheon",
                 eyes: str = "brown",
                 hairs: str = "dark"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        """Return a readable string describing the character."""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __repr__(self) -> str:
        """Return the string representation of the character."""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"


class Lannister(Character):
    """This is a child class of Character, and this has
            family_name, eyes, and hairs as its unique properties,
            and create_lannister() as its unique method."""

    def __init__(self, first_name: str,
                 is_alive: bool = True,
                 family_name: str = "Lannister",
                 eyes: str = "blue",
                 hairs: str = "light"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        """Return a readable string describing the character."""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __repr__(self) -> str:
        """Return the string representation of the character."""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """This constract a new Lannister object and returns it."""

        return cls(first_name, is_alive)
