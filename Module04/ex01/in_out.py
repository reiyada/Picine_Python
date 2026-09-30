def square(x: int | float) -> int | float:
    """This function returns the square value of
        the number that is given."""

    return x ** 2


def pow(x: int | float) -> int | float:
    """This function returns the square value of
        the number that is given."""

    return x ** x


def outer(x: int | float, function) -> object:
    """Return a function that applies function to the previous
        result each time it is called, starting from x."""

    def inner() -> float:
        """Apply the function to the stored value
            and return it."""
        nonlocal x
        x = function(x)
        return x

    return inner
