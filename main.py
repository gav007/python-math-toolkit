from geometry import Circle, Square

def main():
    circle = Circle(5)

    print(circle)
    print("Radius:", circle.get_radius())
    print("Area:", circle.area())
    print("Circumference:", circle.circumference())
    print("Diameter:", circle.diameter())

    print()

    square = Square(4)

    print(square)
    print("Side:", square.get_side())
    print("Area:", square.area())
    print("Perimeter:", square.perimeter())
    
    
if __name__ == "__main__":
    main()