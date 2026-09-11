import numpy as np


def parse_arg(family: list, start: int, end: int):
    """This parse the given argument and check expected errors."""

    assert isinstance(family, list), \
        "A list needs to be given by the argument."
    assert isinstance(start, int) and isinstance(end, int), \
        "Start and End needs to be integers."

    list_len = len(family)

    assert list_len > abs(start) and list_len > abs(end), \
        "Start and End need to be in the range of family."


def handle_slice(family: list, start: int, end: int) -> list:
    """This slices the family list from start index to end index."""

    family_array = np.array(family)
    family_array = family_array[start: end:]

    return family_array.tolist()


def print_result(family: list, sliced_list: list):
    """This prints the expected output."""

    print(f"My shape is : {np.shape(family)}")
    print(f"My new shape is : {np.shape(sliced_list)}")


def slice_me(family: list, start: int, end: int) -> list:
    """This parses the parameter and handle errors,
        then slice the list, print the shape and
        returns the sliced list."""

    try:
        parse_arg(family, start, end)
        sliced_list = handle_slice(family, start, end)
        print_result(family, sliced_list)

        return sliced_list

    except AssertionError as ex:
        print(f"AssertionError: {ex}")
