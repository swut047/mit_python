import calendar as cal
import numpy as np
import math
# import circle

# pi = 3
# print(pi)
# print(circle.pi)
# print(circle.area(3))
# print(circle.circumference(3))
# print(circle.sphere_surface(3))

print(math.log(8, 2))
cal_english = cal.TextCalendar()
print(cal_english.formatmonth(1949, 3))
print(cal.day_name[cal.weekday(2021, 10, 7)])


def find_thanks_giving(year):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]

    else:
        thanksgiving = month[4][cal.THURSDAY]

    return thanksgiving


print('In 2011', ' U.S. Thanksgiving was on November',
      find_thanks_giving(2011))
