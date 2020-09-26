from datetime import datetime
from datetime import date
from datetime import timedelta

print(datetime.today())
# datetime.datetime(2020-09-26 08:20:37.357857)

today = datetime.today()
print(type(today))
# <class 'datetime.datetime'>

todaydate = date.today()
print(todaydate)
# 2020-09-26

print(type(todaydate))
# class 'datetime.date'>

print(todaydate.month)
# 9

print(todaydate.year)
# 2020

print(todaydate.day)
# 26
dashain = date(2020, 10, 18)

print(dashain)
# 2020-10-18

if dashain is not todaydate:
    print("Sorry there are still " + str((dashain - todaydate).days) + " days until dashain!")
else:
    print("It's dashain.")

delta = timedelta(days=50, seconds=27, microseconds=10,
                  milliseconds=29000, minutes=5, hours=8, weeks=2)

print(delta)

p = timedelta(hours=-5)
print(p)