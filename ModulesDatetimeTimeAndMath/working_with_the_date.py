# To get the current date and time, use the datetime.now() method:
from datetime import datetime

now = datetime.now()
print(now)



# As a result of calling the now() method, we get a datetime object that has a number of useful attributes:
current_datetime = datetime.now()

print("\n", current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)

print("\n", current_datetime.date())
print(current_datetime.time(), "\n")



# The datetime object has methods to get the date (without time) and time (without date):
import datetime

date_part = datetime.date(2222, 12, 22)
time_part = datetime.time(22, 22, 22)

combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime, "\n")



# To create a datetime object with a specific date:
specigic_date = datetime.datetime(year=2022, month=2, day=28, hour=22, minute=22, second=22)

print(specigic_date, "\n")



# The weekday() method is used to get the day of the week for the specified date. 
# It returns the day of the week, where Monday is 0 and Sunday is 6 
now = datetime.datetime.now()
day_of_week = now.weekday()

print(f"Today: {day_of_week}")



# To compare two datetime objects in Python, you can use the standard comparison operators
from datetime import datetime

datetime_1 = datetime(5732, 6, 22, 4, 1)
datetime_2 = datetime(5732, 6, 22, 7, 1)

print(datetime_1 == datetime_2) 
print(datetime_1 != datetime_2) 
print(datetime_1 < datetime_2)   
print(datetime_1 > datetime_2)