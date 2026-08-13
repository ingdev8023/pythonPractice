from abc import ABC, abstractmethod
import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height   
    
    def get_area(self):
        return self.height * self.width    
    
    def get_perimeter(self):
        return 2*(self.height + self.width)
    
    def get_diagonal(self):
        return ((self.height ** 2) + (self.width ** 2)) ** 0.5

    def get_picture(self):

        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        return ("*" * self.width + "\n") * self.height
    
    def get_amount_inside(self, obj):
        return math.floor(self.width // obj.width) * (self.height // obj.height)
        
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side
               
    
    def set_width(self, side):
        self.set_side(side)

    def set_height(self, side):
        self.set_side(side)

  
    
    def __str__(self):
        return f'Square(side={self.side})'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
print(Rectangle(15,10).get_amount_inside(Square(5)))
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))
print(Rectangle(2,3).get_amount_inside(Rectangle(3, 6)))