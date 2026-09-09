import sys

def PrintEvenOrOdd():
    assert len(sys.argv) == 2, "more than one argument is provided"

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
        PrintEvenOrOdd()
    except AssertionError as ex:
        print(f"Error: {ex}")



if __name__=="__main__":
    main()