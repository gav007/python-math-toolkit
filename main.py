from geometry import *
from geo_calculations import *

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
                print("This is an invalid Selection")
            else:
                return users_input
        except ValueError:
            print("Not a valid input")
        
def geometry_choice():
    try:
        print("For Square Press (1)")
        print("For Rectangle Press (2)")
        print("For Circle Press (3)")
        print("For Triangle Press (4)")
        print()
        while True:
            print("")
            users_input = int(input("Enter your choice\n"))
            
            
            if users_input < 1 or users_input > 4:
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

        if choice == 1:
            geo_choice = geometry_choice()

            if geo_choice == 1:
                square()
            elif geo_choice == 2:
                rectangle()
            elif geo_choice == 3:
                circle()
            elif geo_choice == 4:
                triangle()
            else:
                print("This value is not accepted.")

        elif choice == 2:
            print("Algebra is not built yet.")

        elif choice == 3:
            print("Calculus is not built yet.")
            
        elif choice == 4:
            print("Goodbye. Program ended.")
            running = False
    
    
if __name__ == "__main__":
    main()