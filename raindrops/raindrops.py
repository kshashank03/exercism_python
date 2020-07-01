def convert(number):
    x = ''
    if number%3 == 0:
        x = 'Pling'
    if number%5 == 0:
        x += 'Plang'
    if number%7 == 0:
        x += 'Plong'
    if len(x) == 0:
        return str(number)
    else:
        return x