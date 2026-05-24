class LinearEquation:
    # Calculates the Y value when given the slope and intercept.
    def __init__(self, slope, intercept):
        self.__slope = 0
        self.__intercept = 0
        
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
        return self.__x1
    
    def set_point_x2(self, x2):
        return self.__x2
    
    def set_point_y1(self, y1):
        return self.__y1
        
    def set_point_y2(self, y2):
        return self.__y2
        
    def calculate_slope(self):
        if (self.__x2 - self.__x1) == 0:
            return "Slope is unfined"
        else:
            m = (self.__y2 - self.__y1) / (self.__x2 - self.__x1)
            return m