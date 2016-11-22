def search(divisor, dividend):
    count = 0
    min = divisor
    max = dividend

    if min < 0:
        min = -(min)
        max = -(max)
    found = False
    midpoint = (max + min) >> 1
    while not found:

        if midpoint * min <= max:
            return midpoint
        else:
            midpoint -= 1

    return max

def divide(numerator, denominator):
    if denominator == 0:
        raise Exception('Cannot divide by zero')

    if denominator == 1:
        return numerator

    if denominator == -1:
        return -(numerator)

    if numerator < 0 and denominator < 0:
        numerator = -(numerator)
        denominator = -(denominator)

    result = search(denominator, numerator)

    if result * denominator != numerator:
        res = [result, numerator - result * denominator]

    else:
        res = result

    return res
