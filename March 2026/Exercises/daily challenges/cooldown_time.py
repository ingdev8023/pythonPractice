""" Cooldown Time
Given two timestamps, the first representing when a user finished an exam, and the second representing the current time, determine whether the user can take an exam again.

Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.
A user must wait at least 48 hours before retaking an exam.
 """

#firstsolution
from datetime import datetime

def can_retake(finish_time, current_time):
    time_cal = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S") - datetime.strptime(finish_time, "%Y-%m-%dT%H:%M:%S")
    return time_cal.total_seconds()/ 3600 >= 48

print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00"))
print(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00"))
print(can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00"))
print(can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59"))



#optimalsolution

from datetime import datetime, timedelta

def can_retake(finish_time, current_time):
    finish = datetime.fromisoformat(finish_time)
    current = datetime.fromisoformat(current_time)
    
    if current < finish:
        return False
    
    return current - finish >= timedelta(hours=48)