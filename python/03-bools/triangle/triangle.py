def is_triangle(a,b,c):
    return a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b

def equilateral(sides):
    a,b,c = sides
    return a == b == c if is_triangle(a,b,c) else False


def isosceles(sides):
    a,b,c = sides
    return (a == b) or (a == c) or (b == c) if is_triangle(a,b,c) else False


def scalene(sides):
    a,b,c = sides
    return (a != b) and (a != c) and (b != c) if is_triangle(a,b,c) else False
