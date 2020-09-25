# Day1 of 100 days of coding.
# Starting from list.
# Accessing Values in Lists.

list1 = ['hi', 'there', 18, 1]
list2 = [1, 2, 3, 4, 5, 6, 7, 8]

print(list1[0])
print(list2[2])

# Updating list
list1[0] = 'ghanshyam'
list1[1] = 'joshi'
list2[7] = 'hi'
print(list1)
print(list2)
list1.append('10')
print(list1)

# Deleting List element
del list1[3]
del list2[7]
print(list1)
print(list2)

# Basic List Operations
# length
value = [1, 2, 'hi']
print(len(value))
print(len([1, 8, 'ji']))

# Concatenation
notvalue = [5, 'no']
new_value = value + notvalue
print(new_value)

# Repetition
hi = ['hi']
print("Value: " +str(hi )* 4 )

# Membership
values = 3
if values in value:
    print("Yes")
else:
    print("no")

# Iteration
for x in [1, 2, 3, 4]:
    print(x)

# Slicing
number = [1, 2, 3, 4]
print(number[4:])

# Function len()
print(len(number))

# Function max()
print(max(number))

# Function min()
print(min(number))

# Function list
no = {'a', 'b'}
print(list(no))