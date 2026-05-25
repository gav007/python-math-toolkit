from geometry import *
from geo_calculations import *
from algebra import *
from algebra_calculations import *
from utils import clear_screen

subjects = ("Geomerty", "Algebra", "Calculas","Exit")

def display(subs):
    print("=" *60)
    #print()
    print("This program performs various Math operations.")
    print("Please select below the calculations you would like to do.")
    print()
    print("=" *60)
    print("Enter value to decide")
    
    for index, sub in enumerate(subs, start=1):
        print(index, sub)
        
def users_choice():
    while True:
        try:
            print()
            users_input = int(input("Enter your choice\n"))
            
            if users_input < 1 or users_input > len(subjects):
                print("This is an invalid selection")
            else:
                return users_input
        except ValueError:
            print("Not a valid input")
        
def geometry_choice():
    while True:
        print("For Square Press (1)")
        print("For Rectangle Press (2)")
        print("For Circle Press (3)")
        print("For Triangle Press (4)")
        print()

        try:
            users_input = int(input("Enter your choice\n"))

            if users_input < 1 or users_input > 4:
                print("This is an invalid selection")
            else:
                return users_input

        except ValueError:
            print("Not a valid input")
        
def algebra_choice():
    while True:
        print("For Linear Equation Press (1)")
        print("For Slope Calculator Press (2)")
        print("For Distance Calculator Press (3)")
        print("For Midpoint Calculator Press (4)")
        print("For Quadratic Equation Press (5)")
        print()

        try:
            users_input = int(input("Enter your choice\n"))

            if users_input < 1 or users_input > 5:
                print("This is an invalid Selection")
            else:
                return users_input

        except ValueError:
            print("Not a valid input")
 
            
def main():
    running = True

    while running:
        display(subjects)
        choice = users_choice()

        # THIS IS FOR THE GEOMETRY CHOICE
        if choice == 1:
            geo_choice = geometry_choice()

            if geo_choice == 1:
                square()
                clear_screen()
            elif geo_choice == 2:
                rectangle()
                clear_screen()
            elif geo_choice == 3:
                circle()
                clear_screen()
            elif geo_choice == 4:
                triangle()
                clear_screen()
            else:
                print("This value is not accepted.")

        # THIS IS FOR THE ALGEBRA CHOICE
        elif choice == 2:
            algebra = algebra_choice()
            
            if algebra == 1:
                cal_linear_equation()
                clear_screen()
            elif algebra == 2:
                slope_calculator()
                clear_screen()
            elif algebra == 3:
                distance_calculator()
                clear_screen()
            elif algebra == 4:
                midpoint_cal()
                clear_screen()
            elif algebra == 5:
                cal_quadratic_equation()
                clear_screen()
            else:
                print("This value is not accepted.")
            

        elif choice == 3:
            print("Calculus is not built yet.")

            
        elif choice == 4:
            print("Goodbye. Program ended.")
            running = False
    
    
if __name__ == "__main__":
    main()