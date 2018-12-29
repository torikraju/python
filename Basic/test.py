my_list=[1,2,3,4,5]
second_list = my_list[0:3]
print(second_list)
second_list[0] = 'hello'
print(second_list)
print(my_list)



stats = [{'name': 'torik'},{'age':'29'}]
print(stats)
copied_stats = stats[:]
copied_stats[0]['name']='alam'
print(copied_stats)
print(stats)


new_list = [True,False,True]
print(any(new_list))
print(all(new_list))

simple_list=[1,2,3,4,-5]
print([el for el in simple_list if el > 0])
print(all([el>0 for el in simple_list]))



simple_list=[1,2,6]
a,b,c = simple_list