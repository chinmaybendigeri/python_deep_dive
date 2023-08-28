import string
# 1. Memberships tests are those tests where you are searching if an element is present in a collection like list,
# tuple, set and dict

# 2. Membership tests are faster when done with set constant expressions instead of list and tuple , this is because
# in case of dict we can find the element directly without going through the list/tuple sequentially until we
# find the element

# 3. Constant Expressions like [1,2,3] gets converted to immutable type tuple (1,2,3) by python and
# {1,2,3} set to frozenset

# 4. Constant Expressions are only calculated once during compilation if the string is of length < 20 for optimizations

import time


def membershipTest(n, container):
    start = time.perf_counter()
    x = 100 * 2
    y = "ab" * 3
    for i in range(n):
        if 'p' in container:
            pass
    end = time.perf_counter()
    print(end - start)


def main():
    listObj = list(string.ascii_letters)
    obj = string.ascii_letters

    tupleObj = tuple(string.ascii_letters)
    setObj = set(string.ascii_letters)

    print(listObj)
    print(tupleObj)
    print(setObj)

    print(membershipTest.__code__.co_consts)
    membershipTest(10000000, listObj)
    membershipTest(10000000, tupleObj)
    membershipTest(10000000, setObj)


if __name__ == "__main__":
    main()
