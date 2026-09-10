import sys


def ft_convert_to_morse(Object: str) -> str:
    """This converts the given argument to the morse code"""

    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",   "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ",    "F": "..-. ", "G": "--. ",  "H": ".... ",
        "I": ".. ",   "J": ".--- ", "K": "-.- ",  "L": ".-.. ",
        "M": "-- ",   "N": "-. ",   "O": "--- ",  "P": ".--. ",
        "Q": "--.- ", "R": ".-. ",  "S": "... ",  "T": "- ",
        "U": "..- ",  "V": "...- ", "W": ".-- ",  "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
        "8": "---.. ", "9": "----. ",
    }

    result = ""

    for c in Object:
        if (c.islower):
            c = c.capitalize()

        morse = NESTED_MORSE[c]

        result += morse

    return result


def ft_parse_str(Object: str):
    """This checks if the given argument is alphanumeric"""

    for c in Object:
        assert c.isnumeric() or c.isalpha() or c == " ", \
            "the arguments are bad"


def ft_print_result():
    """This dispays the result"""

    assert len(sys.argv) == 2, "more than one argument is provided"
    ft_parse_str(sys.argv[1])

    result = ft_convert_to_morse(sys.argv[1])
    print(result)


def main():
    try:
        ft_print_result()
    except AssertionError as ex:
        print(f"Error: {ex}")


if __name__ == "__main__":
    main()
