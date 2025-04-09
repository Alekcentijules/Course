import random
import re
from datetime import datetime, date


def get_days_from_today(transmitted_date):
    """
    Calculated the number of days between today's date and the given date

    Param transmitted_date:
        str: A date string in the format "YYYY.MM.DD"

    Return:
        int: The number of days between today and the given date
    """
    try:
        today = date.today()
        transmitted_date = datetime.strptime(transmitted_date, "%Y.%m.%d").date()
        days = transmitted_date - today
    except ValueError:
        raise ValueError(f"Dates must be in the form: {date.today()}")
    return days.days

def get_numbers_ticket(min, max, quantity):
    """
    Generates a sorted list of unique random numbers within a given range

    Param min:
        int: The minimal number in the range(inclusive)

    Param max:
        int: The maximum number in the range(inclusive)
    Param quantity:
        int: The number of unique random numbers to generate

    Return:
        list: A sorted list of random integers
    """
    try:
        if (max - min) < quantity:
            return []
        num_list = random.sample(range(min, max + 1), quantity)
        num_list.sort()
        return num_list
    except ValueError:
        raise ValueError("Incorrect value entered!")

def normalize_phone(phone_numbers):
    """
    Normalizes a list of phone numbers into international format (+380...)

    Param phone_numbers:
        list: A list of raw phone number strings

    Return:
        list: A list of phone numbers normalized to international format
    """
    try:
        pattern = r"\D"
        clean_list = []
        for num in phone_numbers:
            repleced_list = re.sub(pattern, "", num)
            if repleced_list.startswith("380"):
                clean_list.append("+" + repleced_list)
            elif repleced_list.startswith("0"):
                clean_list.append("+38" + repleced_list)
            else:
                clean_list.append("+" + num)
        return clean_list
    except ValueError:
        raise ValueError("Incorrect value entered!")


# List of raw phone number to normalize
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Test: calculate days from today
first_result = get_days_from_today("2025.05.22")
print(f"Quantity of days: {first_result}")

# Test: generate random lottery numbers
second_result = get_numbers_ticket(1, 1000, 10)
print(f"Your lottery numbers: {second_result}")

# Test: normalize phone number
third_result = normalize_phone(raw_numbers)
print(f"Your phone numbers: {third_result}")
