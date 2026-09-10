import sys


def ft_get_char_count_dict(object: str) -> dict:
    """This count each chars and return the total amount"""

    counter = {"Total": 0,
               "Upper": 0,
               "Lower": 0,
               "Punctuation marks": 0,
               "Spaces": 0,
               "Digits": 0}

    for c in object:
        counter["Total"] += 1

        if (c.isupper()):
            counter["Upper"] += 1
        elif (c.islower()):
            counter["Lower"] += 1
        elif (c == " "):
            counter["Spaces"] += 1
        elif (c.isdigit()):
            counter["Digits"] += 1
        else:
            counter["Punctuation marks"] += 1

    return counter


def ft_print_result():
    """This prints the expected output."""

    assert len(sys.argv) <= 3, "more than one argument is provided"

    if (len(sys.argv) == 1):
        text = input("What is the text to count?\n")
    else:
        text = sys.argv[1]

    result = ft_get_char_count_dict(text)

    print(f"The text contains {result["Total"]} characters:")
    print(f"{result["Upper"]} upper letters")
    print(f"{result["Lower"]} lower letters")
    print(f"{result["Punctuation marks"]} punctuation marks")
    print(f"{result["Spaces"]} spaces")
    print(f"{result["Digits"]} digits")


def main():
    try:
        ft_print_result()
    except AssertionError as ex:
        print(f"Error: {ex}")
    except EOFError:
        print(" ")


if __name__ == "__main__":
    main()
