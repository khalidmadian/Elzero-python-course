def my_func(num1, num2):
    if type(num1) != int or type(num2) != int:
        print('not integer')
    else:
        print(num1 + num2)


my_func(50, 60)

print('-----------------------------')


def full_name(f_name, s_name, l_name):
    print(f'{str(f_name).capitalize().strip()} {str(s_name).upper():.1s} {str(l_name).capitalize().strip()}')


full_name('khalid    ', 'mohamed', 'saad')
