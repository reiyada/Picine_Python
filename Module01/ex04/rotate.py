from load_image import ft_load
from zoom import handle_zoom
import numpy as np
import matplotlib.pyplot as plt


def rotate_image(img_array: np.array) -> np.array:
    """This rotates the array of the given image,
        and return the rotated array."""

    img_array = img_array[:, :, 0]
    height, width = img_array.shape

    rotated_img = np.zeros((width, height), dtype=img_array.dtype)

    for h in range(height):
        for w in range(width):
            rotated_img[h][w] = img_array[w][h]

    return rotated_img


def print_rotated_img_info(rotated_img: np.array):
    """This prints the rotated image information."""

    height, width = rotated_img.shape

    print(f"New shape after Transpose: {height, width}")
    print(rotated_img)


def display_img(img_array: np.array):
    """This displays RGB images from NumPy array."""

    plt.imshow(img_array, cmap="grey")
    plt.show()


def handle_rotation(img_array: np.array):
    """This handles he rotation and prints output."""

    rotated_img = rotate_image(img_array)
    print_rotated_img_info(rotated_img)
    display_img(rotated_img)


def main():
    try:
        img_array = ft_load("animal.jpeg")
        height = 400
        width = 400
        channel = 1
        zoomed_img = handle_zoom(img_array, height, width, channel)
        handle_rotation(zoomed_img)
    except Exception as ex:
        print(f"Error: {ex}")


if (__name__ == "__main__"):
    main()
