age = int(input('Enter Your Age:'))

unit = input('Enter the unit , months,days,hours:').lower().strip()

months = age * 12
days = age * 365
hours = days * 24

if unit == 'months' or unit == 'm':
    print(f'your age is {age}')
    print(f'your age in months is {months:,}')

elif unit == 'days' or unit == 'd':
    print(f'your age is {age}')
    print(f'your age in days is {days:,}')

elif unit == 'hours' or unit == 'h':
    print(f'your age is {age}')
    print(f'your age in hours is {hours:,}')
