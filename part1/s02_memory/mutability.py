# Primitive Data types,Frozen Sets , Tuples are immutable in python Lists, Sets, Dict are mutable datatypes in python
# Note: Immutable types can also change their internal state if its elements are mutable for example tuple containing
# a list as its elements which is mutable type

def main():
    my_list = [1, 2, 3]
    print(hex(id(my_list)))

    my_list.append(3)
    print(hex(id(my_list)))

    t1 = (1, 2)
    print(t1.index(2))

    print(hex(id(t1)))

    t1 = ('a', 'b')
    print(hex(id(t1)))

    t1 = ([1, 2], [3, 4])

    print(hex(id(t1)))
    t1[0].append(5)

    print(hex(id(t1)))


if __name__ == '__main__':
    main()
