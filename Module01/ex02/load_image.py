import numpy as np
from numpy import asarray
from pathlib import Path
from PIL import Image


def parse_path(path: str):
    """This parse the given file path and handle errors."""

    assert isinstance(path, str), "File path needs to be a string."

    file_path = Path(path)
    assert file_path.exists(), "File not found."


def img_to_array(path: str) -> np.array:
    """This load the given file and return it with an array."""

    img = Image.open(path).convert("RGB")
    img_array = asarray(img)

    return img_array


def print_img_info(img_array: np.array):
    """This prints the information fo the image."""

    print(f"The shape of image is: {img_array.shape}")


def ft_load(path: str) -> np.array:
    """This handle the loading the image and return it with an array.
        Also, it prints the information of the image."""

    try:
        parse_path(path)
        img_array = img_to_array(path)
        print_img_info(img_array)

        return img_array

    except (AssertionError, FileNotFoundError, OSError) as ex:
        print(f"Error: {ex}")