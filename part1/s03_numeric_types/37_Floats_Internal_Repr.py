import sys
from fractions import Fraction


def main():
    x = float(3.16)
    print(x)

    x = float("7.98")
    print(x)

    x = float(Fraction("22/7"))
    print(x)

    x = 0.1
    print(x)
    print(format(x, ".25f"))

    print("0.1 == x", format(x, ".25f") == 0.1)  # False => this is because 0.1 in decimal can be stored as finite
    # number in base 2

    y = 0.3
    z = 0.1 + 0.1 + 0.1

    print(y)
    print(z)
    print(y == z)  # False

    print(sys.getsizeof(z))


if __name__ == "__main__":
    main()