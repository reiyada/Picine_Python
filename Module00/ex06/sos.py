import sys


def ConvertToMorse(Object: str) -> str:
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



def ParseStr(Object: str):
    for c in Object:
        assert c.isnumeric() or c.isalpha() or c == " ", "the arguments are bad"


def PrintResult():
    assert len(sys.argv) == 2, "more than one argument is provided"
    ParseStr(sys.argv[1])

    result = ConvertToMorse(sys.argv[1])
    print(result)

def main():
    try:
        PrintResult()
    except AssertionError as ex:
        print(f"Error: {ex}")


if __name__ == "__main__":
    main()
