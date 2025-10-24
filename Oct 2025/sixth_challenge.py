#learning objects and class in python
class Vehicle:
    color = "white"


    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None


    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity


V1 = Vehicle(150, 25)
V1.color = 'red'
print(V1.color)

class Graph():
    def __init__(self, id):
        self.id = id
        self.id = 80


val = Graph(200)
print(val.id)

