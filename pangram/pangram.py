import string, re
def is_pangram(sentence):
    x = re.findall("[A-Za-z]", sentence.lower())
    return set(string.ascii_lowercase) <= set(x)