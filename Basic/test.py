my_list=[1,2,3]
second_list = my_list[:]
print(second_list)
second_list[0] = 'hello'
print(second_list)
print(my_list)