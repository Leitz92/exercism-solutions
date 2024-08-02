"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """This function should return the value of the exchanged currency.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """This function should return the amount of money that *is left* from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value
    


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a single bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """This function should return the _number of currency bills_ that you can receive within the given _amount_.
    In other words:  How many _whole bills_ of currency fit into the starting amount?
    Remember -- you can only receive _whole bills_, not fractions of bills, so remember to divide accordingly.
    Effectively, you are rounding _down_ to the nearest whole bill/denomination.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return int(amount/denomination)


def get_leftover_of_bills(amount, denomination):
    """This function should return the _leftover amount_ that cannot be returned from your starting _amount_ given the denomination of bills.
    It is very important to know exactly how much the booth gets to keep.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """This function should return the maximum value of the new currency after calculating the *exchange rate* plus the *spread*.
    Remember that the currency *denomination* is a whole number, and cannot be sub-divided.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    # Step 1: Convert the spread to a decimal
    spread_decimal = spread / 100
    
    # Step 2: Calculate the actual exchange rate
    actual_exchange_rate = exchange_rate * (1 + spread_decimal)
    
    # Step 3: Determine the total amount in the new currency
    total_new_currency = budget / actual_exchange_rate
    
    # Step 4: Calculate the maximum exchangeable value in terms of the denomination
    max_value = int(total_new_currency // denomination) * denomination
    
    # Step 5: Return the result
    return max_value
    
