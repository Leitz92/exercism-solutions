def square(number):
    """Function that returns how many grains were on a given square.

    :param number: int -> Number of the square.
    :return: int -> Number of grains on the given square number.

    This particular exercise requires that you use the [raise statement] to "throw" a `ValueError` when the square input is out of range.
    """
    # The number must be between 1 and 64.
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    # This code only execute if the number is correct
    return 2 ** (number - 1)


def total():
    """Function that return the total number of grains on the chessboard.

    :return: int -> Total number of grains on the chessboard.
    """
    result = 0
    for x in range (64):
        result += 2**(x)
    return result


