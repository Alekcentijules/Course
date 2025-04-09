# strftime()
from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date: {}".format(formatted_date))

formatted_date_only = now.strftime("%A, %d %B %Y")
print(f"Formatted date only: {formatted_date_only}")

formatted_time_only = now.strftime("%I: %M %p")
print(f"Formatted time only: {formatted_time_only}")

formatted_date_only = now.strftime("%d.%m.%Y")
print(f"Formatted date only: {formatted_date_only} \n")



# strptime()
from datetime import datetime

date_string = "6328.07.22"

datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(f"Datetime object: {datetime_object}")
