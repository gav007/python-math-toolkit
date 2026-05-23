import math

class Circle:
    def __init__(self, radius):
        # radius is the value passed in when we create a Circle object
        self.__radius = radius
        
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
    
     