def main():
    x = 10
    print(type(x))

    def square(x):
        return x**2

    def cube(x):
        return  x**3

    y = square(x) # this is a function call
    z = cube(x)

    print(x,y,z)

    some_func = square # refernce to a function object
    print(type(some_func))

    a = some_func(x)
    print(a)


    def execute_func(func, x):
        print(func(x))

    execute_func(some_func, 15)


if __name__ == "__main__":
    main()