
def checkEquality(a, b):  # always returns true
    print("(a,b) = ({0},{1}) ".format(a, b))
    div = a // b
    mod = a % b
    print("div ", div)
    print("mod ", mod)
    return a == b * div + mod


def main():

    print(checkEquality(13, 4))
    print(checkEquality(-13, 4))
    print(checkEquality(13, -4))
    print(checkEquality(-13, -4))


if __name__ == "__main__":
    main()
