import re
def is_valid(isbn):

    isbn_parse = re.sub("[-]", "", isbn)
    isbn_parse = re.findall("^[0-9]{10}$|^[0-9]{9}[X]$", isbn_parse) #Remove hyphens and match valid patterns for ISBN number

    if len(isbn_parse) != 1 or len(isbn_parse[0]) != 10: #If the parse returns nothing or there aren't 10 characters then reject
        return False
    else: 
        isbn_parse = [i for i in isbn_parse[0]] #Seperate the individual components of the ISBN
        if isbn_parse[9] == "X": #Handle a "X" check character
            isbn_parse[9] = 10
        calculation = sum([int(isbn_parse[i]) * list(range(10, 0, -1))[i] for i in range(10)]) # Sum up the multiplied ISBN numbers
        return calculation % 11 == 0 #Check if the summed number has a mudulo of 0 when divided