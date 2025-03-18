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


def value(colors):
    """Convert a color name to a numerical code.

    :param colors: list - colors of the resistor bands.
    :return: int - numerical code of the color.
    """ 
    # Get the first two colors and map them to the corresponding values
    if len(colors) >= 1:
        first_value = color_code(colors[0])
        second_value = color_code(colors[1])
        return first_value * 10 + second_value
    return None # If there are no colors, then return None
