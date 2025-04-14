def func_1(name, *skills):
    print(f'your name is {name} and your skills is:')

    for skill in skills:
        print(skill)


func_1('khalid', 'python', 'html', 'css')
func_1('omar','flutter','css')
