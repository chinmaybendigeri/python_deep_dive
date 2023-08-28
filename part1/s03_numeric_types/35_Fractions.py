import fractions
import math


def main():
    x = fractions.Fraction("0.125")  # 1/8
    print(x)

    y = fractions.Fraction(0.125)  # you can also pass float to a fraction
    print(y)

    z = fractions.Fraction(1 / 8)  # you can also pass a fraction to a fraction
    print(z)

    a = fractions.Fraction(math.pi)  # 22/7 is not a rational number since it's a recurring number , however in
    # computers these are restricted to a fixed length  after decimal point
    print(a)

    print(a.limit_denominator(100))

    b = math.pi
    print(type(b))


if __name__ == "__main__":
    main()
