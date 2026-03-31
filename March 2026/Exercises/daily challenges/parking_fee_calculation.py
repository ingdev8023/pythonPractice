from datetime import datetime, timedelta
import math

def calculate_parking_fee(park_time, pickup_time):
    park = datetime.strptime(park_time, "%H:%M")
    pickup = datetime.strptime(pickup_time, "%H:%M")

    overnight = False

    if pickup < park:
        pickup += timedelta(days=1)
        overnight = True

    total_time = pickup - park
    hours = math.ceil(total_time.total_seconds() / 3600)

    total_cost = hours * 3

    if overnight:
        total_cost += 10

    if total_cost < 5:
        total_cost = 5

    return f"${total_cost}"