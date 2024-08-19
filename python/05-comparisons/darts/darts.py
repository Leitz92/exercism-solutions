import math

def score(x, y):
    """
    Calculate the points scored in a single toss of a Darts game.

    :param x: float - x coordinate of the dart.
    :param y: float - y coordinate of the dart.
    :return int - points scored.
    """
    # Euclidean Distance: The formula sqrt(x^2 + y^2) calculates the distance
    # from the point (x, y) to the origin (0, 0).

    # Comparison with the radius: If the distance is less than or equal to the radius of the circle, then the point is inside or on the boundary of the circle.

    distance = math.sqrt(x**2 + y**2)
    # Inner circle: 10 points
    if distance <= 1:
        return 10
    # Middle circle: 5 points
    if distance <= 5:
        return 5
    # Outer circle: 1 point
    if distance <= 10:
        return 1
    # Missed: 0 points
    return 0