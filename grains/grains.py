def square(number):
    if number > 0 and number < 65:
        return 2**(number-1)
    else:
        raise ValueError("Need a value between 1 and 64 inclusive")

def total():
    return sum([(2**(x-1)) for x in range(1,65)])
