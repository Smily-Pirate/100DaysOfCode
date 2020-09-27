# DataStructure
numlist = [1, 2, 3, 4, 5]
print(numlist)

numlist.reverse()
print(numlist)
# Gives a reverse list

numlist.sort()
print(numlist)

mystring = "Ghanshyam"

for i in mystring:
    print(i)

l = list(mystring)
t = tuple(mystring)

print(l)
print(t)
l[0] = "b"
print(l)

# t[0] = "m"
print(t)

l.pop()
print(l)

l.insert(5, "n")
print(l)

l.pop(0)
print(l)

l.insert(0, "m")
print(l)

del l[0]


# DICTS

pybites = {'julian': 30, 'bob': 33, 'mike': 33}
print(pybites)

people = {}
people['julian'] = 30
print(people)

people['bob'] = 43
print(people)

print(pybites.keys())
print(pybites.values())

print(pybites.items())

for values in pybites.values():
    print(values)

for keys, values in pybites.items():
    print(keys + str(values))

for keys, values in pybites.items():
    print('%s is %d years of age' % (keys, values))