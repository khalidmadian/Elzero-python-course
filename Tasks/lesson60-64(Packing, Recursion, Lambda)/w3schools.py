def my_func(*kid):  # this is will be lis
    print(f'best child is {kid[2]}')


my_func('khalid', 'saad', 'madian')

print('---------------------------------------')


def func_2(**kid):
    print(f'his last name is {kid["l_name"]}')


func_2(f_name='khalid', l_name='saad')

print('---------------------------------------')


def func_3(*, z):  # (*,)===> force you to put the variable name on the argument
    print(z)


func_3(z=3)
