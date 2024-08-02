"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# define the 'EXPECTED_BAKE_TIME' constant.✅
EXPECTED_BAKE_TIME = 60
# Time in minutes per layer of the lasagna
PREPARATION_TIME = 2

# Remove 'pass' and complete the 'bake_time_remaining()' function below. ✅
def bake_time_remaining(elapsed_bake_time:int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed in minutes.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


# Define the 'preparation_time_in_minutes()' function below. ✅
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers:int):
    """Calculate the preparation time

    :param number_of_layers: int - Number of layers of the lasagna.
    :return: int - Time in minutes you would spend adding the number of layers to the lasagna.

    Function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them.
    Assume each layer takes 2 minutes to prepare.
    """

    return PREPARATION_TIME * number_of_layers

#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
