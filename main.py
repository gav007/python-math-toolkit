from geometry import *

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
    
    triangle = Triangle(10, 5)

    print(triangle)
    print("Base:", triangle.get_base())
    print("Height:", triangle.get_height())
    print("Area:", triangle.area())

    triangle.set_base(20)
    triangle.set_height(8)

    print("\nAfter changing the triangle:")
    print(triangle)
    print("Base:", triangle.get_base())
    print("Height:", triangle.get_height())
    print("Area:", triangle.area())
    
    
if __name__ == "__main__":
    main()