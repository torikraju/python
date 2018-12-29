# * is used for unpacking tuples 
# ** is used for unpacking dictionary 

def unlimited_arguments(*args, **keyword_args):
    print(args,keyword_args)


unlimited_arguments(1, 2, 3, 4, name='torik', age=29)

a = [1, 2, 3]
print('some text: {} {} {}'.format(*a))
