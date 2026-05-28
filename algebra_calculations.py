from algebra import *
from graphing import graph_linear_equation

# Calculates the Linear Equation... 
def cal_linear_equation():
    while True:
        try:
            # get values
            slope = float(input("Enter the known slope value: "))
            intercept = float(input("Enter the known intercept value: "))
            x = float(input("Enter the X value: "))
            
            # create object with values
            linear = LinearEquation(slope, intercept)
            
            # print __str__
            print(linear)
            
            # calculate y 
            y = linear.calculate_y(x)
            
            # set x an y for graphing
            linear.set_x(x)
            linear.set_y(y)
            
            # print slope
            print("Slope:",linear.get_slope())
            
            # print intercept
            print("Intercept:", linear.get_intercept())
            
            # print y calculation
            print("Y value:", round(y,2))
            
            choice = input("Press Enter to try again, g to graph, or q to return to menu: ")

            if choice.lower() == "g":
                graph_linear_equation(linear)                

            elif choice.lower() == "q":
                return
            
        except ValueError:
            print("Value is not an acceptable entry")
            
# Calculates The Slope            
def slope_calculator():
    
    while True:
        try:
            point1 = Point()
            print("Please enter your coordinates below\n")
            
            x1 = float(input("Enter in your X value: "))
            # set x
            point1.set_x(x1)
            
            y1 = float(input("Enter in your Y value: "))
            # set y
            point1.set_y(y1)
            
            point2 = Point()
            print("Now please enter your second set of coordinates below\n")
            
            x2 = float(input("Enter in your X value: "))
            # set x
            point2.set_x(x2)
            
            y2 = float(input("Enter in your Y value: "))
            # set y
            point2.set_y(y2)
            
            slope = SlopeCalculator(
                point1.get_x(),
                point1.get_y(),
                point2.get_x(),
                point2.get_y()
            )
            
            print(point1)
            print(point2)
            print(slope)
            print("Slope:", slope.calculate_slope())
            
            # try again
            try_again = input("Press Enter to try again or q to return to menu: ")
                
            if try_again.lower() == 'q':
                return
            
        except ValueError:
            print("Value is not an acceptable entry")
            
def distance_calculator():
    
    while True:
        try:
            # Create distance object
            distance = DistanceCalculator()
            
            # First point
            point1 = Point()
            print("Please enter your first coordinates below\n")
            
            x1 = float(input("Enter in your X value: "))
            point1.set_x(x1)
            distance.set_point_x1(point1.get_x())
            
            y1 = float(input("Enter in your Y value: "))
            point1.set_y(y1)
            distance.set_point_y1(point1.get_y())
            
            # Second point
            point2 = Point()
            print("Now please enter your second set of coordinates below\n")
            
            x2 = float(input("Enter in your X value: "))
            point2.set_x(x2)
            distance.set_point_x2(point2.get_x())
            
            y2 = float(input("Enter in your Y value: "))
            point2.set_y(y2)
            distance.set_point_y2(point2.get_y())
            
            # Calculate distance
            cal = distance.cal_distance()
            print(distance, "=", round(cal, 2))
            
            # Try again
            try_again = input("Press Enter to try again or q to return to menu: ")
                
            if try_again.lower() == "q":
                return
            
        except ValueError:
            print("Value is not an acceptable entry")
            
def midpoint_cal():
    
    while True:
        try:
            # Create midpoint object
            mid = MidpointCalculator()
            
            # First point
            point1 = Point()
            print("Please enter your first coordinates below\n")
            
            x1 = float(input("Enter in your X value: "))
            point1.set_x(x1)
            mid.set_point_x1(point1.get_x())
            
            y1 = float(input("Enter in your Y value: "))
            point1.set_y(y1)
            mid.set_point_y1(point1.get_y())
            
            # Second point
            point2 = Point()
            print("Now please enter your second set of coordinates below\n")
            
            x2 = float(input("Enter in your X value: "))
            point2.set_x(x2)
            mid.set_point_x2(point2.get_x())
            
            y2 = float(input("Enter in your Y value: "))
            point2.set_y(y2)
            mid.set_point_y2(point2.get_y())
            
            # Calculate midpoint
            # unpack the return tuple
            x,y = mid.cal_midpoint()
            print(mid)
            print(f"Midpoint: ({round(x, 2)}, {round(y, 2)})")
            
            # Try again
            try_again = input("Press Enter to try again or q to return to menu: ")
                
            if try_again.lower() == "q":
                return
            
        except ValueError:
            print("Value is not an acceptable entry")
            
            
def cal_quadratic_equation():
    
    while True:
        try:
            # Create quadratic object
            quad = QuadraticEquation()
            
            # Point for x and y result
            point = Point()
            
            print("Please enter your quadratic values below\n")
            
            a = float(input("Enter the a coefficient (x squared value): "))
            quad.set_a(a)
            
            b = float(input("Enter the b coefficient (x value): "))
            quad.set_b(b)
            
            c = float(input("Enter the c constant value: "))
            quad.set_c(c)
            
            x = float(input("Enter the x input value: "))
            point.set_x(x)
            
            # Calculate y
            y = quad.cal_quad(point.get_x())
            point.set_y(y)
            
            print(quad)
            print(point)
            print("Y value:", round(point.get_y(), 2))
            
            try_again = input("Press Enter to try again or q to return to menu: ")
                
            if try_again.lower() == "q":
                return
            
        except ValueError:
            print("Value is not an acceptable entry")