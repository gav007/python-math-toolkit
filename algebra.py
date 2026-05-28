import math
class LinearEquation:
    # Calculates the Y value when given the slope and intercept.
    def __init__(self, slope, intercept):
        self.__slope = 0
        self.__intercept = 0
        self.__x = 0
        self.__y = 0
        
        self.set_slope(slope)
        self.set_intercept(intercept)
        
    def get_slope(self):
        return self.__slope

    def get_intercept(self):
        return self.__intercept

    def set_slope(self, slope):
        self.__slope = slope

    def set_intercept(self, intercept):
        self.__intercept = intercept
        
    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        self.__y = y

    def get_y(self):
        return self.__y
    
    def calculate_y(self, x):
        y = self.__slope * x + self.__intercept
        return y
    
    def __str__(self):
        return f"Linear equation: y = {self.__slope}x + {self.__intercept}"
    
class SlopeCalculator:
    # Calculates the slope of the line
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = 0
        self.__y1 = 0
        self.__x2 = 0
        self.__y2 = 0
        
        self.set_point_x1(x1)
        self.set_point_x2(x2)
        self.set_point_y1(y1)
        self.set_point_y2(y2)
        
        
    def get_point_x1(self):
        return self.__x1
    
    def get_point_x2(self):
        return self.__x2
    
    def get_point_y1(self):
        return self.__y1
    
    def get_point_y2(self):
        return self.__y2
    
    def set_point_x1(self, x1):
        self.__x1 = x1
    
    def set_point_x2(self, x2):
        self.__x2 = x2
    
    def set_point_y1(self, y1):
        self.__y1 = y1
        
    def set_point_y2(self, y2):
        self.__y2 = y2
        
    def calculate_slope(self):
        if (self.__x2 - self.__x1) == 0:
            return "Slope is unfined"
        else:
            m = (self.__y2 - self.__y1) / (self.__x2 - self.__x1)
            return m
        
    def __str__(self):
        return f"Slope between ({self.__x1}, {self.__y1}) and ({self.__x2}, {self.__y2})"

class Point:
    
    def __init__(self):
        self.__x = 0
        self.__y = 0
        
    def set_x(self, x):
        self.__x = x
        
    def set_y(self, y):
        self.__y = y
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
        
    def __str__(self):
        return f"Point({self.__x}, {self.__y})"
    
    
class DistanceCalculator:
    
    def __init__(self):
        self.__x1 = 0
        self.__x2 = 0
        self.__y1 = 0
        self.__y2 = 0
    
    def get_point_x1(self):
        return self.__x1
    
    def get_point_x2(self):
        return self.__x2
    
    def get_point_y1(self):
        return self.__y1
    
    def get_point_y2(self):
        return self.__y2
    
    def set_point_x1(self, x1):
        self.__x1 = x1
    
    def set_point_x2(self, x2):
        self.__x2 = x2
    
    def set_point_y1(self, y1):
        self.__y1 = y1
        
    def set_point_y2(self, y2):
        self.__y2 = y2
        
    def cal_distance(self):
        d = math.sqrt((self.__x2-self.__x1)**2+(self.__y2-self.__y1)**2)
        return d
    
    def __str__(self):
        return f"Distance between ({self.__x1}, {self.__y1}) and ({self.__x2}, {self.__y2})"
    
class MidpointCalculator:
    
    def __init__(self):
        self.__x1 = 0
        self.__x2 = 0
        self.__y1 = 0
        self.__y2 = 0
    
    def get_point_x1(self):
        return self.__x1
    
    def get_point_x2(self):
        return self.__x2
    
    def get_point_y1(self):
        return self.__y1
    
    def get_point_y2(self):
        return self.__y2
    
    def set_point_x1(self, x1):
        self.__x1 = x1
    
    def set_point_x2(self, x2):
        self.__x2 = x2
    
    def set_point_y1(self, y1):
        self.__y1 = y1
        
    def set_point_y2(self, y2):
        self.__y2 = y2
        
    def cal_midpoint(self):
        x = (self.__x1 + self.__x2)/2
        y = (self.__y1 + self.__y2)/2
        mid = (x, y)
        return mid
    
    def __str__(self):
        return f"Midpoint between ({self.__x1}, {self.__y1}) and ({self.__x2}, {self.__y2})"
    
class QuadraticEquation:
    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.__c = 0
        
    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def get_c(self):
        return self.__c
    
    def set_a(self, a):
        if a == 0:
            print("a cannot be 0 as this will make it linear")
        else:
            self.__a = a
            
    def set_b(self, b):
        self.__b = b
        
    def set_c(self, c):
        self.__c = c
        
    def cal_quad(self, x):
        y = self.__a *x ** 2 + self.__b * x + self.__c
        return y
    
    def __str__(self):
        return f"Quadratic equation: y = {self.__a}x^2 + {self.__b}x + {self.__c}"