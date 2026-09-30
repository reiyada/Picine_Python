from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """This is a child class that inherits from both Baratheon and
        Lannister, and has its unique methods."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """This is the constructor of king class
            which inisializes its properties."""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def set_eyes(self, eyes: str):
        """This sets the eye color to the given color."""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """This sets the hair color to the given color."""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """This returns the king's eye color."""
        return self.eyes

    def get_hairs(self) -> str:
        """This returns the king's hair color."""
        return self.hairs
