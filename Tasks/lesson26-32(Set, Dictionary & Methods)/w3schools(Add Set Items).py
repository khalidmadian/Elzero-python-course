hi_man={'hi',True,50,'hi'}

print('hi'in hi_man)

# ===========================================
print("="*50)


my_set={'ahmed','safwat','kareem'}
my_set.add('khalid')
my_set.add('zizo')
print(my_set)

# ===========================================
print("="*50)

# To add items from another set into the current set, use the update() method.

my_set.update(hi_man)
print(my_set)

# ===========================================
mylist=['sosan','loaa','taha']

my_set.update(mylist)

print(my_set)



