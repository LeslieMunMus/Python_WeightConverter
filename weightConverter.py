# This is a program that takes a user input weight and askes for the
#   metric unit used and converts it to the corresponding unit

import os

os.system("clear")

# I am using %0.2f to format a float to 2 decimal places

"""
def main():
    weight = float(input("Weight: "))
    unit = input("(L)bs or (K)g: ")

    if unit.upper() == "K":
        calc = weight / 0.45
        print("You are %0.2f pounds" % (calc))
    elif unit.upper() == "L":
        calc = weight * 0.45
        print("You are %0.2f kilograms" % (calc))
    else:
        print("The unit you entered is not supported")


if __name__ == "__main__":
    main()
"""

# This version emulates a C++ do...while loop for better control


def main():
    while True:
        weight = float(input("Enter weight: "))
        unit = input("Enter 'L' for Lbs or 'K' for Kg: ")

        if unit.upper() == "K":
            calc = weight / 0.45
            print("You weigh %0.2f pounds" % (calc))
            break
        elif unit.upper() == "L":
            calc = weight * 0.45
            print("You weigh %0.2f kilograms" % (calc))
            break
        else:
            if unit.upper() != "K" or unit.upper() != "L":
                print("You have entered a wrong metric unit. Please try again.")


if __name__ == "__main__":
    main()
