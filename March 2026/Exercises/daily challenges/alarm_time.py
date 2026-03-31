""" Wake-Up Alarm
Given a string representing the time you set your alarm and a string representing the time you actually woke up, determine if you woke up early, on time, or late.

Both times will be given in "HH:MM" 24-hour format.
Return:

"early" if you woke up before your alarm time.
"on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
"late" if you woke up more than 10 minutes after your alarm time.
Both times are on the same day. """


#from datetime import datetime

def alarm_check(alarm_time, wake_time):

    alarm_minutes = (int(alarm_time[:2]) * 60) + int(alarm_time[3:])       
    wake_minutes = (int(wake_time[:2]) * 60) + int(wake_time[3:])    
    

    if wake_minutes < alarm_minutes:
        return "early"
    elif wake_minutes <= alarm_minutes + 10:
        return "on time"
    else:
        return "late"


    #wake = datetime.strptime(wake_time, "%H:%M")
    #alarm = datetime.strptime(alarm_time, "%H:%M")

    #final_time = (wake - alarm).total_seconds() / 60

    #if final_time <  - 10:
    #    return "early"
    #elif final_time > 10:
    #    return "late"
    #else:
    #    return 'on time'    

print(alarm_check("07:00", "06:45"))
print(alarm_check("06:30", "06:30"))
print(alarm_check("09:30", "09:45"))
print(alarm_check("08:15", "08:25"))
print(alarm_check("08:10", "08:15"))