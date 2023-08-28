import fractions


# n = 232
# b = 5
# 1 , 4, 1, 2

def from_base10(n, b):
    if b < 2:
        raise ValueError("Base b must be >= 2")
    if n < 0:
        raise ValueError("Number n must be >= 0")
    if n == 0:
        return [0]
    else:
        base_repr = []
        while n > 0:
            m = n % b
            n = n // b
            base_repr.insert(0, m)
        return base_repr


def encoding(digits, encoding_map):
    if max(digits) >= len(encoding_map):
        raise ValueError("encoding map is not long enough to do encoding")
    else:
        encoded = ''
        for d in digits:
            print(d)
            encoded += encoding_map[d]
    return encoded


def main():
    a = int("1010", 2)
    print(a)

    b = int(196.988)
    print(b)

    b = int(-196.988)
    print(b)

    x = 22
    y = 7

    z = fractions.Fraction(x,y)

    print(z)
    print(float(z))

    base_rpr = from_base10(232, 5)

    print(encoding(base_rpr, '01234'))


if __name__ == "__main__":
    main()
