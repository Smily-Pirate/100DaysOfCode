import random

# random.choice()... chose from the given list
x = random.choice([1, 2, 3, 5, 6])
print(x)

for new in range(1, 10):
    # randrange generates a random number from a given set of numbers
    y = random.randrange(20, 50, 3)
    print(y)

# Maps a particular random number with the seed argument.
random.seed(5)

# generates a float random number less than 1 or greater or equal to 0
print(random.random())
n = [3, 4, 1, 6, 7]

# shuffle the list
random.shuffle(n)
print(n)

for i in range(0, 100):
    print(random.randrange(3, 6))

x: int = random.randrange(1, 50)
y: int = random.randrange(2, 5)
z = x**y
print(z)
