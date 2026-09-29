from abc import ABC, abstractmethod


class Character(ABC):
    """This is a parent class that has first_name and
        is_alive as its property, and die() as its method."""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """This is the constructor of Character class
            which inisializes its properties."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """This is a method of Character class which
            changes the value of is_alive to the oposite."""

        self.is_alive = not self.is_alive


class Stark(Character):
    """This is a child class that inherits Character class."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """This is the constructor of Stark class
            which calls the constructor of Character class."""
        super().__init__(first_name, is_alive)
