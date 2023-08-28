import ctypes
import gc
import time


# circular references are automatically handled by gc in python version >= 3.4 , circular references to occur when one
# instance A is referring an object B and B is referring to object A as shown in the below example.
class A:
    def __init__(self):
        self.b = B(self)
        print("Instance A: s02_memory address of A {0}, s02_memory address of B {1}".format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print("Instance B: s02_memory address of B {0}, s02_memory address of A {1}".format(hex(id(self)), hex(id(self.a))))


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(address_id):
    for obj in gc.get_objects():
        if id(obj) == address_id:
            return "Object Exists"
    return "Not Found"


def main():
    my_var = A()

    a_id = id(my_var)
    b_id = id(my_var.b)

    print(hex(a_id))
    print(hex(b_id))

    print(ref_count(a_id))
    print(ref_count(b_id))

    print(object_by_id(a_id))
    print(object_by_id(b_id))
    gc.disable()

    my_var = None

    print(ref_count(a_id))
    print(ref_count(b_id))

    print(object_by_id(a_id))
    print(object_by_id(b_id))

    gc.collect()

    print(ref_count(a_id))
    print(ref_count(b_id))

    print(object_by_id(a_id))
    print(object_by_id(b_id))

    time.sleep(5)

    print(ref_count(a_id))


if __name__ == "__main__":
    main()
