n = int(input("Enter the number"))

for i in range(0, n):
    for j in range(0, i + 1):
        print("* ", end="")

    print("\r")


def pypart(n):
    myList = []
    for i in range(1, n + 1):
        myList.append("*" * i)
    print("\n".join(myList))


pypart(n)

# 180 degree rotation
def funfun(n):
    # number of spaces
    k = 2 * n - 2

    # outer loop to handle number of rows
    for i in range(0, n):
        # inner loop to handle number
        # values changing acc to required spaces
        for j in range(0, k):
            print(end=" ")
        # Decrementing k after each loop
        k = k - 2

        # inner loop to handle number
        # values changing acc to outer loop
        for j in range(0, i + 1):
            print("* ", end="")

        print("\r")

funfun(n)


# Continue....................



