def is_even(number:int):
    """This function say if a given number is even (true) or odd (false)

    :param number: int - Positive number
    :return: bool - True if the number is even, False if odd
    """
    return number%2 == 0

def steps(number:int):
    number = int(number)  # Convert input into number

    # check if the number is 0 or lower
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    # Only execute if the number is correct
    result = 0
    while number != 1:
        if is_even(number):
            number /= 2
        else:
            number = number*3 + 1
        result += 1
    return result