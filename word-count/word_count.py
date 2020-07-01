import re
def count_words(sentence):
    the_dict = {}
    sentence = re.findall("[a-z0-9]+['][a-z0-9]+|[a-z0-9]+", sentence.lower())
    for i in sentence:
        the_dict[i] = sentence.count(i)
    return the_dict