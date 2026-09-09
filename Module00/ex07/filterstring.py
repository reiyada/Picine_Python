import sys


def GetStrList() -> list:
    """This returns the list of the words that are longer than given number"""
    assert len(sys.argv) == 3

    textList = sys.argv[1].split()
    count = int(sys.argv[2])

    return [word for word in textList if (lambda w: len(w) > count)(word)]


def PrintResult():
    """This prints the expected output"""
    result = GetStrList()

    print(result)


def main():
    try:
        PrintResult()
    except AssertionError:
        print("the arguments are bad")
    except ValueError:
        print("the arguments are bad")


if __name__ == "__main__":
    main()
