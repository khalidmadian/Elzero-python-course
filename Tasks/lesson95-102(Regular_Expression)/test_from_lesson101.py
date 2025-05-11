import re

my_string = re.split(r'_|"', 'khalid_set_in_x-space_working"space _.')

print(my_string)
for counter, word in enumerate(my_string, 1):
    if len(word) == 1:
        continue
    else:
         print(f'{counter} => {word.capitalize()}')

print('########################################################')

my_string='I Love Python And Css'

print(re.sub(r'\s','-',my_string,2))