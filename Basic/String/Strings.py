my_list = ['h', 'e', 'l', 'l', 'o']
my_text = 'hello'

# Loop through string
# for el in my_text:
#     print(el)


# String is immutable example
# my_text[0] = 'w'
# print(my_text)


name = 'torik'
age = 29

print('i am {} and i am {} years old'.format(name, age))
print('i am {0} and i am {1} years old. i really an named {0}'.format(name, age))
print('i am {name} and i am {years} years old. i really an named {name}'.format(name=name, years=age))

funds = 15.039723
print('Funds : {:.2f}'.format(funds))
print('Funds : {:10.2f}'.format(funds))
print('Funds : {:^10.2f}'.format(funds))
print('Funds : {:-^10.2f}'.format(funds))

# for more format specification mini-language
