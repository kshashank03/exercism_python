import re
def abbreviate(words):
    
    clean_word = re.sub("-", " ", words)
    clean_word = re.sub("[^a-zA-Z\s]", repl="", string=clean_word)

    return "".join([i[0].upper() for i in re.findall("[a-zA-Z]+", string=clean_word)])