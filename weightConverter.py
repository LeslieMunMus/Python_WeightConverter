import os

os.system("clear")

# I am using %0.2f to format a float to 2 decimal places


def main():
    weight = float(input("Weight: "))
    metric_symbol = input("(L)bs or (K)g: ")

    if metric_symbol.upper() == "K":
        calc = weight / 0.45
        print("You are %0.2f pounds" % (calc))
    elif metric_symbol.upper() == "L":
        calc = weight * 0.45
        print("You are %0.2f kilograms" % (calc))
    else:
        print("The metric symbol you entered is not supported")


if __name__ == "__main__":
    main()
