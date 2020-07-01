def is_armstrong_number(number):
    number_list = [int(x) for x in str(number)]
    return sum(list(map(lambda x: x**len(number_list), number_list))) == number