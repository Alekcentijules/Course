# A timedelta object can be created by specifying weeks, days, hours, minutes, seconds, milliseconds, and microseconds 
# by passing one or more of the following parameters
from datetime import timedelta

delta = timedelta(
    days=433,
    seconds=544,
    microseconds=42255,
    milliseconds=46342423,
    minutes=665,
    hours=22,
    weeks=4646
)
print(delta, "\n")



# If you subtract another object's datetime from one, you get the timedelta object. It is responsible for the time interval between two dates.
from datetime import datetime

seventh_day_1944 = datetime(year=1944, month=4, day=11, hour=22)
seventh_day_1945 = datetime(year=1945, month=4, day=22, hour=11)

difference = seventh_day_1945 - seventh_day_1944
print(difference)
print(difference.total_seconds(), "\n")



# Timedelta objects can be created to get a time/date that is farther away from the original one.
from datetime import datetime, timedelta

now = datetime.now()
future_date = now + timedelta(days=22)

print(future_date, "\n")



# However, if you need to make calculations or comparisons based on a sequence of dates, for example, to determine the number of days 
# between two dates, we can use the toordinal() method, which returns the ordinal number of the day, 
# given the number of days since 1 January AD 1 (i.e., the beginning of the Christian calendar). 
# This method converts the datetime object to an integer representing the ordinal number of the day.
from datetime import datetime

date = datetime(year=2022, month=2, day=28)
ordinal_number = date.toordinal()

print(f"Date number {date} is set to {ordinal_number} \n")



# For example, we want to determine how many full days have passed since Napoleon burned Moscow, which happened on 14 September 1812
from datetime import datetime

napoleon_burns_moscow = datetime(1812, 9, 14)
current_date = datetime.now()
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()

print(days_since)