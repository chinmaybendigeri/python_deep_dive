import sys
from math import isclose


def main():
    a = 0.01
    b = 0.02

    print(isclose(a, b, rel_tol=0.01, abs_tol=0.0001))

    a = 0.0000001
    b = 0.0000002

    print(isclose(a, b, rel_tol=0.01, abs_tol=0.0001))

    a = 123456789.01
    b = 123456789.02

    print(isclose(a, b, rel_tol=0.01, abs_tol=0.0001))


if __name__ == "__main__":
    main()
