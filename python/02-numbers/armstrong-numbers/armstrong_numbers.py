def is_armstrong_number(number):
    """Function that determines whether a given number is an Armstrong number or not.

    :param number: int -> Positive number.
    :return: bool -> True if is an Armstrong number, False otherwise.

    An [Armstrong number] is a number that is the sum of its own digits each raised to the power of the number of digits.
    """
    # Case the given number is negative
    if number < 0:
        return False
    # Case the number is correct
    result = 0
    number_str = str(number)
    number_length = len(number_str)
    for digit in number_str:
        result += int(digit) ** number_length
    return result == number

