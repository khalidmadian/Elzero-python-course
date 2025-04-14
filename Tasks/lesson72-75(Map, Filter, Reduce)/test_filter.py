def fiter_num(num):
    return num > 10


my_iterable = [20, 30, 7, 2, 50, 3]
my_filter = filter(fiter_num, my_iterable)
for item in my_filter:
    print(item)

print('-------------------------------------------------')

name_iterable = ['khalid', 'kareem', 'kenan', 'saad', 'safwat', 'meroo']

my_name_filter = list(filter(lambda name: str(name).startswith('k'),name_iterable))
print(my_name_filter)