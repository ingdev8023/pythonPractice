# Weekday Finder
# Given a string date in the format YYYY-MM-DD, return the day of the week.

# Valid return days are:

# "Sunday"
# "Monday"
# "Tuesday"
# "Wednesday"
# "Thursday"
# "Friday"
# "Saturday"
# Be sure to ignore time zones.

from datetime import date


def get_weekday(date_string):
    weekday_list = ["Sunday","Monday","Tuesday","Wednesday",
"Thursday","Friday","Saturday"]
    date_formatted = date.fromisoformat(date_string)
    
    return weekday_list[date.isoweekday(date_formatted)]

print(get_weekday("2025-11-06"))
print(get_weekday("1999-12-31"))
print(get_weekday("1111-11-11"))
print(get_weekday("2112-12-21"))