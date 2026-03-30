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