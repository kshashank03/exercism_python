def commands(number):
    counter = 0
    return_list = []
    commands_list = ['wink', 'double blink', 'close your eyes', 'jump', 'reverse']
    for i in list(str(bin(number))[2:])[::-1]:
        if i == "1":
            return_list.append(commands_list[counter])
        counter+=1
    if counter == 5:
        return_list.reverse()
        del return_list[0]
        return return_list
    else: 
        return return_list