def recite(start, take=1):
    verses=[]
    for i in range(start, start-take, -1):
        if i > 1:
            verses.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        elif i == 1:
            verses.append(f"{i} bottle of beer on the wall, {i} bottle of beer.")
        else:
            verses.append("No more bottles of beer on the wall, no more bottles of beer.")

        if i > 2:
            verses.append(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")
            if i > start - take + 1:
                verses.append("")
        elif i == 2:
            verses.append(f"Take one down and pass it around, 1 bottle of beer on the wall.")
            if i > start - take + 1:
                verses.append("")
        elif i == 1:
            verses.append("Take it down and pass it around, no more bottles of beer on the wall.")
            if i > start - take + 1:
                verses.append("")
        else:
            verses.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return verses