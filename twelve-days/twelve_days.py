def recite(start_verse, end_verse):
    
    def verse_creator(verse):
        day_number = {1:'first', 2:'second', 3:'third', 4:'fourth', 
                    5:'fifth', 6:'sixth', 7:'seventh', 8:'eighth', 
                    9:'ninth', 10:'tenth', 11:'eleventh', 12:'twelfth'}.get(verse)

        song_start = f"On the {day_number} day of Christmas my true love gave to me: "

        if verse == 1:
            first_day = ''
        else:
            first_day = 'and '

        song = [f'{first_day}a Partridge in a Pear Tree.',
                'two Turtle Doves, ',
                'three French Hens, ',
                'four Calling Birds, ',
                'five Gold Rings, ',
                'six Geese-a-Laying, ',
                'seven Swans-a-Swimming, ',
                'eight Maids-a-Milking, ',
                'nine Ladies Dancing, ',
                'ten Lords-a-Leaping, ',
                'eleven Pipers Piping, ',
                'twelve Drummers Drumming, '] 
        return_song = []
        return_song.append(song_start)
        
        for i in list(range(verse))[::-1]:
            return_song.append(song[i])
        return ''.join(return_song)
    final_output = []
    [final_output.append(verse_creator(i)) for i in range(start_verse, end_verse + 1)]
    return final_output
