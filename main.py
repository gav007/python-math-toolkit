from geometry import Circle

def main():
    
    my_circle = Circle(5)
    
    print(my_circle)
    
    print("Radius:", my_circle.get_radius())
    print("Area:", my_circle.area())
    print("Circumference:", my_circle.circumference())
    print("Diameter:", my_circle.diameter())
    
    my_circle.set_radius(10)
    
    print("The radius had now changed:")
    
    print(my_circle)
    print("Radius:", my_circle.get_radius())
    print("Diameter:", my_circle.diameter())
    print("Area:", my_circle.area())
    print("Circumference:", my_circle.circumference())
    
if __name__ == "__main__":
    main()