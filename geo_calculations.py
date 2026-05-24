from geometry import *

def circle():
    while True:
        try:
            # get radius
            print("Enter your radius: ")
            radius = float(input(">> "))
        
            if radius > 0:
                # create object
                circle = Circle(radius)
                # print radius
                print("Radius:", circle.get_radius())
                # get circumference
                print("Circumference:", round(circle.circumference(),2))
                # get area
                print("Area:", round(circle.area(),2))
                
                try_again = input("Press Enter to try again or q to return to menu: ")
                
                if try_again.lower() == 'q':
                    return
                
            else:
                print("The radius must be greater than 0")
            
        except ValueError:
            print("Not a valid entry")
            
def square():
    while True:
        try:
            # get side
            print("Enter your length: ")
            length = float(input(">> "))
        
            if length > 0:
                # create object
                square = Square(length)
                # print radius
                print("Length:", square.get_side())
                # get circumference
                print("Perimeter:", round(square.perimeter(),2))
                # get area
                print("Area:", round(square.area(),2))
                
                try_again = input("Press Enter to try again or q to return to menu: ")
                
                if try_again.lower() == 'q':
                    return
                
            else:
                print("The Length must be greater than 0")
            
        except ValueError:
            print("Not a valid entry")
            
def triangle():
    while True:
        try:
            # get side
            print("Enter your height: ")
            height = float(input(">> "))

            print("Enter your base: ")
            base = float(input(">> "))
            
            if height > 0 and base > 0:
                # create object
                triangle = Triangle(base, height)
                # print base
                print("Base:", triangle.get_base())
                # get height
                print("Height:", triangle.get_height())
                # get area
                print("Area:", round(triangle.area(),2))
                
                try_again = input("Press Enter to try again or q to return to menu: ")
                
                if try_again.lower() == 'q':
                    return
                
            else:
                print("The Length must be greater than 0")
            
        except ValueError:
            print("Not a valid entry")        
    
def rectangle():
    while True:
        try:
            # get side
            print("Enter your length: ")
            length = float(input(">> "))
            
            print("Enter your width: ")
            width = float(input(">> "))

            
            if length > 0 and width > 0:
                # create object
                rectangle = Rectangle(length, width)
                # print base
                print("Length:", rectangle.get_length())
                # print width
                print("Width:", rectangle.get_width())
                # get perimeter
                print("Perimeter:", round(rectangle.perimeter(),2))
                # get area
                print("Area:", round(rectangle.area(),2))
                
                try_again = input("Press Enter to try again or q to return to menu: ")
                
                if try_again.lower() == 'q':
                    return
                
            else:
                print("The Length must be greater than 0")
            
        except ValueError:
            print("Not a valid entry") 