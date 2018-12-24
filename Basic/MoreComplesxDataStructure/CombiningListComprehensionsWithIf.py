simple_list = [1, 2, 3, 4]

dup_list = [el for el in simple_list if el % 2 == 0]

print(dup_list)

calc_items = [1, 2,67]

dup_list = [el for el in simple_list if el in calc_items]

print(dup_list)
