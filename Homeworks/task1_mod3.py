from datetime import datetime, date

def get_days_from_today(transmitted_date):
    try:
        today = date.today()
        transmitted_date = datetime.strptime(transmitted_date, "%Y.%m.%d").date()
        days = transmitted_date - today
    except ValueError:
        raise ValueError(f"Dates must be in the form: {date.today()}")
    return days.days

result = get_days_from_today("2025.05.22")
print(f"Quantity of days: {result}")