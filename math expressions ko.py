def div(a, b):
    """Return the result of dividing a by b."""
    d = a / b
    return d


def sub(a, b):
    """Return the result of subtracting b from a."""
    l = a - b
    return l


def sum(a, b):
    """Return the sum of a and b."""
    s = a + b
    return s


def flooordivide(a,b):
    """returns the floor division of a and b."""
    d = a//b
    return d


def avr(a, b):
    """Print the average of a and b."""
    s = sum(a, b)
    A = division(s)
    print(A)


avr(1, 5)


def multiply(a, b):
    """Return the product of a and b."""
    m = a * b
    return m


def area(a, b):
    """Return the area of a rectangle given sides a and b."""
    a = multiply(a, b)
    return a


a = area(1, 5)
print(a)


def perimeter(a, b):
    """Return the perimeter of a rectangle given sides a and b."""
    P = 2 * sum(a, b)
    return P


x = 5
y = 9
P = perimeter(x, y)
print(P)


def triangelelelelelelelelelelelelelelelelelelelelele(a, b):
    """Return the area of a triangle given base a and height b."""
    m = multiply(a, b)
    T = division(m)
    return T


T = triangelelelelelelelelelelelelelelelelelelelelele(x, y)
print(T)


def pt(a, b):
    """Return the hypotenuse of a right triangle with sides a and b."""
    q = multiply(a, a)
    w = multiply(b, b)
    s = sum(q, w)
    C = s ** 0.5
    return C


C = pt(y, x)
print(C)


def quad(a, b, c):
    """
    Solve the quadratic equation ax^2 + bx + c = 0 using the quadratic formula.
    
    Returns:
        tuple: The two roots (x1, x2) of the quadratic equation.
    """
    o = 0
    d = sub(multiply(b, b), multiply(a, c) * 4) ** 0.5
    print(d)
    v = sub(o, b) + d
    g = sub(o, b) - d
    print(v)
    x1 = div(v, multiply(2, a))
    x2 = div(g, multiply(2, a))
    return x1, x2


q = quad(1, 2, 3)
print(q)
