class Car:
    wheels = 4

    def __init__(self, color):
        self.color = color

ferrari = Car('red')

print(ferrari.wheels)
print(ferrari.color)
print(Car.wheels)


class Dog:
    def __init__(name, age):
        self.name = name
        self.age = age

dog = Dog("Pinky", 3)
print(dog.name)