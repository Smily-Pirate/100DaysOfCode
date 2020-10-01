import math

def Diamond(rows):
    n = 0
    for i in range(1, rows + 1): # Goes from 1 , 2, 3
        for j in range(1, (rows - i) + 1): # j changes with i
            print(end= " ") # prints empty space
            #print(end = " ")

        while n != (2 * i -1): # value changes with i
            print("*", end = "") # prints *
            n = n + 1
        n = 0

        print()

    k = 1
    n = 1
    for i in range(1, rows):
        for j in range(1, k + 1):
            print(end= " ")
            #print(end = " ")
        k = k + 1

        while n <= (2 * (rows - i) - 1):
            print("*", end = "")
            n = n + 1
        n = 1
        print()


rows = 4
Diamond(rows)




def circle(radius):

    # dist represents distance  to the center
    for i in range((2 * radius)+1):
        for j in range((2 * radius)+1):

            dist = math.sqrt((i - radius) * (i - radius) +
                             (j - radius) * (j - radius))

            if (dist > radius - 0.5 and dist < radius + 0.5):
                print("*",end="")
            else:
                print(" ", end="")

        print()

radius = 6
circle(radius)





