
nums = int(input())
n = ' '
upper_value = int(nums - 2)
lower_value = 1
for x in range(0, nums):
    if lower_value <= x <= upper_value:
        print("*",6*n, "*")
    else:
        print("*"*10)


value = int(input("Enter the number."))
for triangle in range(0, value):
    print("*"*triangle)

x = (512 - 282)/(47*48 + 5)
print(x)


number_one = int(input())
number_two = int(input())
number_three = int(input())
total = number_one + number_two + number_three
print(total)
average = total/3
print(average)


for value in range(0, 1):
    x = "A"*5
for next_value in range(0, 1):
    y = "B"*5

z = x + y
print(z)


for not_triangle in range(5, 0, -1):
    print("*"*not_triangle)


for diamond in range(1, 5):
    if(2 % diamond == 0):
        print("*")