class calculator:
    """This is calculator class that has 4 methods
        and one property."""

    def __init__(self, numbers: list[float]):
        """This is a constructor of Calculator class
            that inits numbers."""
        self.numbers = numbers

    def __add__(self, object) -> None:
        """This calculate addition to each int
            of the property numbers."""

        result = []
        for n in self.numbers:
            result.append(n + object)

        self.numbers = result
        print(self.numbers)

    def __mul__(self, object) -> None:
        """This calculate multiplication to each int
            of the property numbers."""
        result = []
        for n in self.numbers:
            result.append(n * object)

        self.numbers = result
        print(self.numbers)

    def __sub__(self, object) -> None:
        """This calculate subtraction to each int
            of the property numbers."""
        result = []
        for n in self.numbers:
            result.append(n - object)

        self.numbers = result
        print(self.numbers)

    def __truediv__(self, object) -> None:
        """This calculate true division to each int
            of the property numbers."""
        try:
            result = []
            for n in self.numbers:
                if n == 0:
                    raise ValueError("0 cannot be divided.")
                result.append(n / object)
        except ValueError as ex:
            print(f"Error: {ex}")

        self.numbers = result
        print(self.numbers)
