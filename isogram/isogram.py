def is_isogram(string):
    string = string.replace("-", "")
    string = string.replace(" ", "")
    string = string.lower()
    return len(set(string)) == len(string)