# Without list comprehensions
list_input = [1, 2, 3, 4, 5, 6, 7]
list_output = []

for var in list_input:
    if var % 2 == 0:
        list_output.append(var)

print(list_output)

# With list comprehension
list_list = [1, 2, 3, 4, 5, 6, 7, 8]

list_using_comp = [var for var in list_list if var % 2 == 0]
print(list_using_comp)

# Constructing output list using for loop
output_list = []
for var in range(1, 10):
    output_list.append(var ** 2)
print(output_list)


output_list_comp = [var ** 2 for var in range(1, 10)]
print(output_list_comp)

# Dictionary Comprehensions
new_list = [1, 2, 3, 4, 5]
output_dict = {}
for var in new_list:
    if var % 2 != 0:
        output_dict[var] = var ** 3
    print(output_dict)


dict_using_comp = {var:var ** 3 for var in new_list if var % 2 != 0}
print(dict_using_comp)

state = ['kathmandu', 'maharajgunj']
capital = ['idk', 'hahah']

out_dict = {}

for (key, value) in zip(state, capital):
    out_dict[key] = value
print(out_dict)


dict_us_co = {key:value for (key, value) in zip(state, capital)}
print(dict_us_co)
