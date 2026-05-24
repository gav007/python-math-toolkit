from geometry import *

def main():
    rectangle = Rectangle(10, 5)

    print(rectangle)
    print("Length:", rectangle.get_length())
    print("Width:", rectangle.get_width())
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())

    rectangle.set_length(20)
    rectangle.set_width(8)

    print("\nAfter changing the rectangle:")
    print(rectangle)
    print("Length:", rectangle.get_length())
    print("Width:", rectangle.get_width())
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())

    
    
if __name__ == "__main__":
    main()