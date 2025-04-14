users = ['kareem', 'hosaam', 'refaat', 'khalid']
admins = ['khalid']

name = input('what is is your name:').lower().strip()
prove_admin = 'no'

if name in admins:
    options_1 = input('Edit in admins ->(admins_u) , other users->(other_u):').lower().strip()
    if options_1 == 'admins_u':
        a_option_1_1 = input('delete account->(d), update your name->(u), add new admin user->(a)').lower().strip()
        if a_option_1_1 == 'd':
            admins.pop(admins.index(name))
            print(f"the new admins list is {admins}")
        elif a_option_1_1 == 'u':
            current_admin_name = input('enter your new name:').lower().strip()
            admins[admins.index(name)] = current_admin_name
            print(f"the new admins list is {admins}")
        elif a_option_1_1 =='a':
            new_a_name=input('Enter new admin name:').lower().strip()
            admins.append(new_a_name)
            print(f"the new admins list is {admins}")
        else:
            print('wrong inputs')


    elif options_1 == 'other_u':
        option_u_1 = input('delete user->(d) ,add user->(a) ,update user name->(u)')
        if option_u_1 == 'd':
            delete_user_name = input('Enter user name you want to delete:').lower().strip()
            users.pop(users.index(delete_user_name))
            print(f"the new users list is {users}")
        elif option_u_1 == 'a':
            added_user_name = input('Enter user name you want to add: ').lower().strip()
            users.append(added_user_name)
            print(f"the new users list is {users}")
        elif option_u_1 == 'u':
            update_user_name = input('Enter user name you want to update:').lower().strip()
            new_user_name = input('Enter the new name:').lower().strip()
            users[users.index(update_user_name)] = new_user_name
            print(f"the new users list is {users}")
        else:
            print('wrong inputs')

elif name in users:
    option_u_2 = input('delete my user name->(d), update my user name->(u)')
    if option_u_2 == 'd':
        users.pop(users.index(name))
        print(f"the new users list is {users}")
    elif option_u_2 == 'u':
        new_user_name = input('Enter the new name:').lower().strip()
        users[users.index(name)] = new_user_name
        print(f"the new users list is {users}")
    else:
        print('wrong inputs')


else:
    print("you are not sign in you want to signout")
