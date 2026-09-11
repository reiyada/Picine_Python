import sys

def ft_print_even_or_odd():
    assert len(sys.argv) <= 2, "more than one argument is provided"

    if (len(sys.argv) == 1):
        return

    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if (num % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    try:
        ft_print_even_or_odd()
    except AssertionError as ex:
        print(f"AssertionError: {ex}")



if __name__=="__main__":
    main()