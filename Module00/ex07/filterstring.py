import sys


def ft_get_str_list() -> list:
    """This returns the list of the words that are longer than given number"""

    assert len(sys.argv) == 3

    textList = sys.argv[1].split()
    count = int(sys.argv[2])

    return [word for word in textList if (lambda w: len(w) > count)(word)]


def ft_print_result():
    """This prints the expected output"""

    result = ft_get_str_list()

    print(result)


def main():
    try:
        ft_print_result()
    except AssertionError:
        print("the arguments are bad")
    except ValueError:
        print("the arguments are bad")


if __name__ == "__main__":
    main()
