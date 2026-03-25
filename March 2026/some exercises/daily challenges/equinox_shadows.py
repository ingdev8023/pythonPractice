""" Equinox Shadows
Today is the equinox, when the sun is directly above the equator and perfectly overhead at noon. Given a time, determine the shadow cast by a 4-foot vertical pole.

The time will be a string in "HH:MM" 24-hour format (for example, "15:00" is 3pm).
You will only be given a time in 30 minute increments.
Rules:

The sun rises at 6am directly "east", and sets at 6pm directly "west".
A shadow always points opposite the sun.
The shadow's length (in feet) is the number of hours away from noon, cubed.
There is no shadow before sunrise (before 6am), after sunset (6pm or later), or at noon.
Return:

If a shadow exists, return "(length)ft (direction)". For example, "8ft west".
Otherwise, return "No shadow".
For example, given "10:00", return "8ft west" because 10am is 2 hours from noon, so 23 = 8 feet, and the shadow points west because the sun is in the east at 10am. """


from datetime import datetime

def get_shadow(time):
    actual_time = datetime.strptime(time, "%H:%M")
    sunrise_time = datetime.strptime('6:00', "%H:%M")
    sunset_time = datetime.strptime('18:00', "%H:%M")
    noon_time = datetime.strptime('12:00', "%H:%M")
    shadow_direction = ''   
    if actual_time >= sunrise_time and actual_time < sunset_time and actual_time != noon_time:
        if actual_time < noon_time:
            shadow_direction = 'west'
        else:
            shadow_direction = 'east'
        shadow_time = abs(actual_time - noon_time)
        shadow_length = ((shadow_time.total_seconds()) / 3600)**3    
        return f"{shadow_length:g}ft {shadow_direction}"    
    else: 
        return "No shadow"    
    
    

print(get_shadow("10:00"))
print(get_shadow("15:00"))
print(get_shadow("12:00"))
print(get_shadow("17:30"))
print(get_shadow("05:00"))
print(get_shadow("06:00"))
print(get_shadow("18:00"))
print(get_shadow("00:00"))



#chat solution

def get_shadow(time):
    hours = int(time[:2])
    minutes = int(time[3:])
    total_hours = hours + minutes / 60

    if total_hours < 6 or total_hours >= 18 or total_hours == 12:
        return "No shadow"

    direction = "west" if total_hours < 12 else "east"
    shadow_length = abs(total_hours - 12) ** 3

    return f"{shadow_length:g}ft {direction}"