"""What Day Is It?
Given a Unix timestamp in milliseconds, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.
"""

from datetime import datetime, timezone
def get_day_of_week(timestamp):
    real_dt = datetime.fromtimestamp(timestamp/1000, timezone.utc)
    return real_dt.strftime("%A")


print(get_day_of_week(1775492249000))
print(get_day_of_week(1766246400000))
print(get_day_of_week(33791256000000))
print(get_day_of_week(0))