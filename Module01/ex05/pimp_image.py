import array
from load_image import display_img


def ft_invert(array) -> array:
    """Inverts the color of the image received."""

    result = 255 - array
    display_img(result, "ft_invert")
    return result


def ft_red(array) -> array:
    """Convert the color of the image received to red.
        Keep the red channel and set green and blue to 0. """

    result = array * [1, 0, 0]
    display_img(result, "ft_red")
    return result


def ft_green(array) -> array:
    """Convert the color of the image received to green.
        Keep green and remove red and blue.. """

    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    display_img(result, "ft_green")
    return result


def ft_blue(array) -> array:
    """Convert the color of the image received to blue.
        Keep blue and remove red and green."""

    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    display_img(result, "ft_blue")
    return result


def ft_grey(array) -> array:
    """Convert the color of the image received to grey."""

    result = array.copy()
    result[:, :, 1] = result[:, :, 0]
    result[:, :, 2] = result[:, :, 0]
    display_img(result, "ft_grey")
    return result
