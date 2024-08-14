def convert(number):
    """
    Convert a number to its raindrop sound representation.

    :param number: int - the number to convert.
    :return: str - the raindrop sound representation.
    """
    raindrop = ""
    if number % 3 == 0:
        raindrop += "Pling"
    if number % 5 == 0:
        raindrop += "Plang"
    if number % 7 == 0:
        raindrop += "Plong"
    return raindrop if raindrop else str(number)
