age = int(input('Enter Your Age').strip())

print(age)
print('You Lived For:')

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f'{months} Months ')
print(f'{weeks:,} Weeks ')
print(f'{days:,} Days ')
print(f'{hours:,} Hours ')
print(f'{seconds:,} seconds ')
