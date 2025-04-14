tries = 4
password = 'kha'
in_pass = input('Enter your password')

while password != in_pass:
    tries -= 1
    in_pass = input(f'wrong pass Try Again {"last" if tries == 0 else tries} chance left')
    if tries == 0:
        print('cant login again')
        break

else:
    print('logged in')
