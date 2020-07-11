import os

os.system("clear")

# I am using %0.2f to format a float to 2 decimal places


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
