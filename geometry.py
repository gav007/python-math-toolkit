import math

class Circle:
    
    def __init__(self, radius):
        # radius is the value passed in when we create a Circle object
        self.__radius = 0
        self.set_radius(radius)
             
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be greater than 0")
        
    def area(self):
        return math.pi * self.__radius **2
    
    def circumference(self):
        return 2 * math.pi * self.__radius
    
    def diameter (self):
        return self.__radius * 2
    
    def __str__(self):
        return f"Circle with radius {self.__radius}"
    
     
class Square:
    
    def __init__(self, side):
        # calculates the square
        self.__side = 0
        self.set_side(side)
        
    def get_side(self):
        return self.__side
    
    def set_side(self, side):
        if side > 0:
            self.__side = side
        else:
            print("The side must be greater than 0")
            
    def __str__(self):
        return f"Square with length of {self.__side}"
    
    def area(self):
        return self.__side ** 2
    
    def perimeter(self):
        return self.__side * 4
    
    
class Triangle:
    # takes two parameters.... 
    def __init__(self, base, height):
        self.__base = 0
        self.__height = 0
        # pass setter directly into the init
        self.set_base(base)
        self.set_height(height)
        
    def set_base(self, base):
        if base > 0:
            self.__base = base
        else:
            print ("Base must be greater than 0")
            
    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            print ("Height must be greater than 0")
            
    def get_base(self):
        return self.__base
    
    def get_height(self):
        return self.__height
    
    def area(self):
        area = 0.5 * self.__base * self.__height
        return area
    
    def __str__(self):
        return f"Triangle with base of {self.__base} and height of {self.__height}"
    
    