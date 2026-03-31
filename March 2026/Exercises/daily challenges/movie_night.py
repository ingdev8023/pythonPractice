""" Movie Night
Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the total cost of the movie tickets for that showing.

The given day will be one of:

"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
"Sunday"
The showtime will be given in the format "H:MMam" or "H:MMpm". For example "10:00am" or "10:00pm".

Return the total cost in the format "$D.CC" using these rules:

Weekend (Friday - Sunday): $12.00 per ticket.
Weekday (Monday - Thursday): $10.00 per ticket.
Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
Tuesdays: all tickets are $5.00 each. """

from datetime import datetime

def get_movie_night_cost(day, showtime, number_of_tickets):
    
    if not day or not showtime or number_of_tickets is None:
        return "Missing Input"

    days_prices = {
        "Friday": 12.00,
        "Saturday": 12.00,
        "Sunday": 12.00,
        "Monday": 10.00,
        "Tuesday": 5.00,
        "Wednesday": 10.00,
        "Thursday":10.00
         }
    
    movie_time = datetime.strptime(showtime, "%I:%M%p") 
    matinee_time = datetime.strptime("5:00pm","%I:%M%p")
    price_per_ticket = days_prices[day]

    if day != "Tuesday" and movie_time < matinee_time:
        price_per_ticket -= 2.00

    total = price_per_ticket * number_of_tickets

    return f'${total:.2f}'

print(get_movie_night_cost("Saturday", "10:00pm", 1) )
print(get_movie_night_cost("Sunday", "10:00am", 1))
print(get_movie_night_cost("Tuesday", "7:20pm", 2))
print(get_movie_night_cost("Wednesday", "5:40pm", 3))
print(get_movie_night_cost("Monday", "11:50am", 4))
print(get_movie_night_cost("Tuesday", "11:30am", 1))