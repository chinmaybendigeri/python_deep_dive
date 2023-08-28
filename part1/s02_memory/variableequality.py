import sys

def main():
    a = 10
    b = 10
    print("a is b", a is b)  # True
    print("a == b", a == b)  # True

    a = 5000
    b = 5000
    print("a is b", a is b)  # True
    print("a == b", a == b)  # True

    a = [1, 2, 3]
    b = [1, 2, 3]
    print("a is b", a is b)  # False because list is a mutable object ..mutable objects creates two different objects
    # even though the contents are the same
    print("a == b", a == b)  # True

    print(id(None))

    a = None
    b = None
    print("a is None", a is None)
    print("a == None", a == None)
    print("a is b", a is b)
    print(id(a))

    a = 10
    b = 10.0
    if isinstance(a, int):
        print("hello")

    print(type(b))

    print("a is b", a is b)
    print("a == b", a == b)



    S1 = sys.intern("This \
    string is being \
    interned")
    S2 = sys.intern("This \
    string is being \
    interned")

    print("S1 is S2 ", S1 is S2)


if __name__ == "__main__":
    main()