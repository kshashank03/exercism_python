import re
def response(hey_bob):
    if hey_bob[-1] == "?":
        if hey_bob.upper() == hey_bob:
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure"
    elif hey_bob.upper() == hey_bob:
        return "Whoa, chill out!"
    elif len(hey_bob) == 0 or re.match("/w", hey_bob) == None:
        return "Fine. Be that way!"
    else:
        return "Whatever"