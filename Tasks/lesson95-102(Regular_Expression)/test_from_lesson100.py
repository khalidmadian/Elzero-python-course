
# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------

import re


my_search = re.search('\w{4}','Khalid abo elfetoh')
print(my_search)
print(my_search.span())
print(my_search.group())
print(my_search.string)

while True:
    is_email = input('Enter your email: ')
    my_email = re.search(r'^[A-z0-9\.]+@(gmail|hotmail)+\.(com|net)', is_email)

    if my_email is None:
        print('Your Email Is Not Valid')

    else:
        print(f'your email is Valid Here"{my_email.string}"')

