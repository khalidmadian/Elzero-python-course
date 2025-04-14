# my_short_fun = lambda a, x: a + x
# print(my_short_fun(5,6))

my_iterable = ['khalid', 'saad', 'kareem', 'omar']

def my_func(text):
    return f'Ramadan Kareem {text} :)'


my_mapping = list(map(my_func, my_iterable))
print(my_mapping)

print('---------------------another way for mapping--------------------------')

for item in map(my_func, my_iterable):
    print(item)
