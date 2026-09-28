from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def display_img(img_array: np.array):
    """This displays RGB images from NumPy array."""

    plt.imshow(img_array, cmap="grey")
    plt.show()


def parse_size_info(height: int, width: int, channel: int):
    """This parse the size infromation and raise the error if needed."""

    assert isinstance(height, int) and isinstance(width, int) \
        and isinstance(channel, int), "Size need to be integers."
    assert height >= 0 and width >= 0 and channel >= 0, \
        "Size need to be positive numbers."


def slice_image(img_array: np.array, height: int, width: int, channel: int)\
        -> np.array:
    """Zoom the given image and return its array."""

    parse_size_info(height, width, channel)

    ori_y, ori_x, ori_c = img_array.shape

    # start_y = (ori_y - height) // 2
    # start_x = (ori_x - width) // 2
    start_y = 100
    start_x = 450

    zoomed_image = img_array[start_y:start_y + height,
                             start_x:start_x + width, 0: channel]
    return zoomed_image


def print_zoomed_img_info(zoomed_img: np.array, height: int,
                          width: int, channel: int):
    """This prints the zoomed image info"""

    print(f"New shape after slicing: {height, width,\
                                      channel} or {height, width}")
    print(f"{zoomed_img}")


def handle_zoom(img_array: np.array, height: int, width: int, channel: int)\
        -> np.array:
    try:
        zoomed_img = slice_image(img_array, height, width, channel)
        print_zoomed_img_info(zoomed_img, height, width, channel)
        display_img(zoomed_img)

        return zoomed_img
    except Exception as ex:
        print(f"Error: {ex}")


def main():

    try:
        img_array = ft_load("animal.jpeg")
        height = 400
        width = 400
        channel = 1
        handle_zoom(img_array, height, width, channel)
    except Exception as ex:
        print(f"Error: {ex}")


if (__name__ == "__main__"):
    main()
