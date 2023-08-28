def main():
    print("Inside the main Function")

    x = [1, 2, 3]
    val = 10
    ind = 0
    while ind < len(x):
        if x[ind] == val:
            break
        ind += 1
    else:  # here the else block gets executed only if the while loop didn't encounter the break
        x.append(val)

    print(x)


if __name__ == "__main__":
    main()
