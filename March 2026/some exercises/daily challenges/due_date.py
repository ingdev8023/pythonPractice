""" Due Date
Given a date string, return the date 9 months in the future.

The given and return strings have the format "YYYY-MM-DD".
If the month nine months into the future doesn't contain the original day number, return the last day of that month. """


from datetime import datetime
from dateutil.relativedelta import relativedelta

def due_date(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date + relativedelta(months=9)
    return new_date.strftime("%Y-%m-%d")

print(due_date("2025-03-30"))


#chat's
def get_due_date(date_str):
    
    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def days_in_month(year, month):
        if month == 2:
            return 29 if is_leap(year) else 28
        elif month in [4, 6, 9, 11]:
            return 30
        return 31

    year, month, day = map(int, date_str.split("-"))

    new_month = month + 9
    new_year = year + (new_month - 1) // 12
    new_month = (new_month - 1) % 12 + 1

    max_day = days_in_month(new_year, new_month)

    if day > max_day:
        day = max_day

    return f"{new_year:04d}-{new_month:02d}-{day:02d}"
    
print(get_due_date("2025-03-30"))
print(get_due_date("2025-05-29"))