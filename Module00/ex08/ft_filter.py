
def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for
    which function(item) is true. If function is None,
    return the items that are true."""
    for i in iterable:
        if (function(i)):
            yield i


def main():
    result = ft_filter(lambda x: x % 2 == 0, range(1, 11))
    print(list(result))


if (__name__ == "__main__"):
    main()
