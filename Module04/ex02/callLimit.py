def callLimit(limit: int):
    """A function that takes as argument a call limit of
        another function and blocks its execution above a limit."""
    count = 0

    def callLimiter(function):
        """Wrap function so its calls are counted and limited."""

        def limit_function(*args: any, **kwds: any):
            """An inner function to be called if the count
                is less than the limit."""
            nonlocal count
            count += 1
            if (count <= limit):
                return function(*args, **kwds)
            else:
                print(f"Error: {function} called too many times")

        return limit_function

    return callLimiter
