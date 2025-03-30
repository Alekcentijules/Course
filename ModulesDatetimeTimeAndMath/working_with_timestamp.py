# In Python, you can convert a datetime object to a timestamp and vice versa. 
# Converting datetime to timestamp
from datetime import datetime

now = datetime.now()
timestamp = datetime.timestamp(now)

print(timestamp, "\n")



# Converting a timestamp to a datetime object
from datetime import datetime

timestamp = 9999999999
dt_object = datetime.fromtimestamp(timestamp)

print(dt_object, "\n")