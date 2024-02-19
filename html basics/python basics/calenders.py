import calendar
print(calendar.weekheader(3))# number indicates length of the header
print(calendar.firstweekday())# py considers monday as first day
print(calendar.month(2019,9)) # prints the calender of the month specified.(month=sep)
print(calendar.monthcalendar(2019,9))
print(calendar.calendar(2022)) # the entire calender of the year
day_of_the_week = calendar.weekday(2022,9,29)
print(day_of_the_week)
is_leap=calendar.isleap(2020)
print(is_leap)
how_many_leap_days=calendar.leapdays(2000,2005)
print(how_many_leap_days) # since 2000 is leap year. here the second parameter is exclusive.
