# ============================================
# 1. Basic Arithmetic Functions
# ============================================

def subtract(a, b):
    """Return the result of subtracting b from a."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the result of dividing a by b. Raises ZeroDivisionError if b = 0."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def floor_divide(a, b):
    """Return the result of floor division a // b."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a // b


def modulus(a, b):
    """Return the remainder of dividing a by b."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a % b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


# Tests
print("Section 1 Tests:")
print(subtract(10, 4))     # 6
print(multiply(3, 5))      # 15
print(divide(10, 2))       # 5.0
print(floor_divide(10, 3)) # 3
print(modulus(10, 3))      # 1
print(power(2, 3))         # 8
print()


# ============================================
# 2. Combining Operators
# ============================================

def average(a, b):
    """Return the average of a and b."""
    return divide(add(a, b), 2)


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def area_rectangle(length, width):
    """Return the area of a rectangle."""
    return multiply(length, width)


def perimeter_rectangle(length, width):
    """Return the perimeter of a rectangle."""
    return multiply(2, add(length, width))


# Tests
print("Section 2 Tests:")
print(average(4, 6))             # 5.0
print(area_rectangle(4, 5))      # 20
print(perimeter_rectangle(4, 5)) # 18
print()


# ============================================
# 3. More Complex Formulas
# ============================================

def area_triangle(base, height):
    """Return the area of a triangle (½ × base × height)."""
    return divide(multiply(base, height), 2)


def pythagoras(a, b):
    """Return the hypotenuse of a right triangle with sides a and b."""
    return power(add(power(a, 2), power(b, 2)), 0.5)


def quadratic_roots(a, b, c):
    """
    Return the two solutions (roots) of a quadratic equation ax^2 + bx + c = 0.
    Formula: x = (-b ± sqrt(b² - 4ac)) / (2a)
    """
    discriminant = power(b, 2) - 4 * a * c
    if discriminant < 0:
        return None, None  # no real roots
    sqrt_d = power(discriminant, 0.5)
    root1 = divide(-b + sqrt_d, 2 * a)
    root2 = divide(-b - sqrt_d, 2 * a)
    return root1, root2


# Tests
print("Section 3 Tests:")
print(area_triangle(4, 6))   # 12
print(pythagoras(3, 4))      # 5.0
print(quadratic_roots(1, -3, 2))  # (2.0, 1.0)
print()


# ============================================
# 4. Challenge Exercises
# ============================================

def distance(x1, y1, x2, y2):
    """Return the distance between two points (x1, y1) and (x2, y2)."""
    return power(power(x2 - x1, 2) + power(y2 - y1, 2), 0.5)


def bmi(weight, height):
    """Return the Body Mass Index (BMI) given weight (kg) and height (m)."""
    return divide(weight, power(height, 2))


def celsius_to_fahrenheit(c):
    """Convert Celsius temperature to Fahrenheit."""
    return (c * 9/5) + 32


# Tests
print("Section 4 Tests:")
print(distance(0, 0, 3, 4))       # 5.0
print(bmi(70, 1.75))              # ~22.86
print(celsius_to_fahrenheit(0))   # 32.0
print()


# ============================================
# 5. Calculating Easter Date
# (Using the Anonymous Gregorian Algorithm)
# ============================================

def easter_date(year):
    """
    Return the date of Easter Sunday for a given year (Gregorian calendar).
    Uses the 'Anonymous Gregorian algorithm'.
    """
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return f"{year}-{month:02d}-{day:02d}"


# Test
print("Section 5 Tests:")
print(easter_date(2025))  # 2025-04-20
print()


# ============================================
# 6. Additional Formulas
# ============================================

def circle_area(radius):
    """Return the area of a circle given its radius."""
    pi = 3.141592653589793
    return pi * power(radius, 2)


def circle_circumference(radius):
    """Return the circumference of a circle given its radius."""
    pi = 3.141592653589793
    return 2 * pi * radius


# Tests
print("Section 6 Tests:")
print(circle_area(5))          # ~78.54
print(circle_circumference(5)) # ~31.42
