def is_valid(isbn):
    """
    Check if the given ISBN is valid.

    :param isbn: str - the input ISBN
    :return: bool - True if the ISBN is valid, False otherwise
    """
    # Remove the dashes from the ISBN string
    isbn_parsed = isbn.replace('-', '')
    # Check if the ISBN string has 10 charactrers
    if len(isbn_parsed) != 10:
        return False
    # Get the last digit of the ISBN string
    check_digit = isbn_parsed[-1]
    # Check if the ISBN string without the last digit has numbers only
    if not isbn_parsed[:-1].isdigit():
        return False
    # convert the check digit into a int value
    if check_digit == 'X':
        check_digit = 10
    elif check_digit in ('0123456789'):
        check_digit = int(check_digit)
    else:
        return False
    # Calculate the formula to validate the ISBN
    count = 10
    result = 0
    for i in range(0, len(isbn_parsed)-1):
        result += count * int(isbn_parsed[i])
        count -= 1
    # add the check digit to the result
    result += check_digit
    # check if the result is divisible by 11
    return result % 11 == 0
