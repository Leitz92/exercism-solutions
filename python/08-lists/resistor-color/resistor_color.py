def color_code(color):
    """Convert a color name to a numerical code.

    :param color: str - name of the color.
    :return: int - numerical code of the color.
    """
    color_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    return color_map.get(color)


def colors():
    """Returns a list of the different band colors.

    :return: list - of color names.
    """
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
