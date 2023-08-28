# python has different numeric data types (5 Types) such as Integer Numbers , Rational Numbers, Real Numbers,
# Complex Numbers , Boolean Type

import sys


def main():
    x = 10 + 20  # int
    y = 20 - 100  # int
    z = 10 ** 2  # int
    a = 10 * 5  # int
    b = 100 / 10  # float

    print(b)
    print(type(b))

    print(sys.getsizeof(a))  # 28 bytes is allocated to store integer value, 4 bytes is allocated to store the actual
    # number and remaining 24 bytes is the overhead in creating an instance of int


if __name__ == "__main__":
    main()
