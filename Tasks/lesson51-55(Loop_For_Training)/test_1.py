peoples = {
    'khalid': {
        'HTML': '80%',
        'css': '80%',
        'pyhon': "50%"
    },
    'ahmed': {
        'HTML': '0%',
        'css': '0%',
        'pyhon': "20%"
    },
    'omar': {
        'HTML': '50%',
        'css': '50%',
        'pyhon': "30%"
    }
}
for name in peoples:
    print(f'{name}' )
    for skills in peoples[name]:
        print(f'{skills} => {peoples[name][skills]} ')
