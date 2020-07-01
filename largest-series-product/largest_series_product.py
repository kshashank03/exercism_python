import math
def largest_product(series, size):
    if size < 0:
        raise ValueError("Can't have negative values")
    products = [] 
    for i in range(len(series) - size + 1):
        result = 1
        for n in range(size):
            result = result * int(series[i + n])
        products.append(result)
    return max(products)