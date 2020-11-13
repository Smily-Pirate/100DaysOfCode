test_dict = {"Gfg": 3,  "is": 5, "for": 8, "Geeks": 10, "Best": 16}
print("The original dictionary is : " + str(test_dict))
sub_list = [5, 4, 10, 20, 16]
res = dict()
for key in test_dict:
    if test_dict[key] in sub_list:
        res[key] = test_dict[key]


    print("Extracted items : " + str(res))