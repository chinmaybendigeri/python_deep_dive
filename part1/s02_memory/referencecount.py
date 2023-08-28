
import sys
def main():
    my_var = [1,2,3]

    print(sys.getrefcount(my_var))

    b = my_var
    print(sys.getrefcount(my_var))

    my_var = [4,5,6]
    print(sys.getrefcount(b))


if __name__ == "__main__":
    main()