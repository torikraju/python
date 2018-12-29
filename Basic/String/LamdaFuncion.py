simple_list = [1, 2, 3, 4]


# map is faster than list comprehension
print(list(map(lambda el: el * 2, simple_list)))
