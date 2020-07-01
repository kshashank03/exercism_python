import calendar
from datetime import date

day_of_week_dict = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}
week_dict = {"1st":[1], "2nd":[2], "3rd":[3], "4th":[4], "5th":[5], "teenth":[13, 14, 15, 16, 17, 18, 19]}

def meetup(year, month, week, day_of_week):
    c = [i for i in calendar.Calendar().itermonthdays2(year, month)]

    day_list = [tup for tup in c if tup[1] == day_of_week_dict.get(day_of_week) and tup[0]!=0]
    week_list = [tup for tup in day_list if tup[0] in week_dict.get(week)]

    return date(year, month, week_list[0][0])
