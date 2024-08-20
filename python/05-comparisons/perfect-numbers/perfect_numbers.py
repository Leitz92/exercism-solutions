def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # if a number to be classified is less than 1.
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    # Get the divisors of the number.
    divisors = [i for i in range(1,number//2 +1) if number % i == 0]
    # Calculate the sum of divisors.
    sum_of_divisors = sum(divisors)
    # Classify the number based on the sum of divisors.
    if sum_of_divisors == number:
        return "perfect"
    if sum_of_divisors < number:
        return "deficient"
    # Last case
    return "abundant"
