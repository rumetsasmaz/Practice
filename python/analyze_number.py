def analyze_number(number):

    if number % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    square = number ** 2
    cube = number ** 3

    division = number // 3
    remainder = number % 3

    return parity, square, cube, division, remainder
print(analyze_number(10))  # Example usage