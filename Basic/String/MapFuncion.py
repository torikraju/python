simple_list = [1, 2, 3, 4]


def multiply(el):
    return el * 2


# map is faster than list comprehension
print(list(map(multiply, simple_list)))
