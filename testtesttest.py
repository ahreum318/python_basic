import datetime
import time

now = datetime.datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)

today = datetime.date.today()
print(today)

weekday = today.weekday()

# if weekday == 0:
#     pass
# elif weekday == 1:
#     pass...
# ㄴ방법이 너무 무식함

week = ["월","화","수","목","금","토","일"] # 0:월

print(week[weekday])

xmas = datetime.datetime(2026, 12, 25)
print(week[xmas.weekday()])

print(xmas - today)