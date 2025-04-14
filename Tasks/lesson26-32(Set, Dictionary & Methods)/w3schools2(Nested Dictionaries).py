my_family = {
    'wife': {
        'name': 'amal',
        'age': 50
    }   ,
    'child1': {
        'name': 'khalid',
        'age': 24
    }  ,
    'child2': {
        'name': 'tasneem',
        'age': 18
    }

}
for x,obj in my_family.items():
    print(x)
    for y in obj:
        print(f'{y} : {obj[y]}')