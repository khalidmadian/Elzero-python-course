my_set={'hi',True,50,'hi'}

my_set.remove('hi')

print(my_set)
# Note: If the item to remove does not exist, remove() will raise an error.

# =========================================
print(50*'=')

set_1={'tota','haila','khalid',10,246}

set_1.discard('mariam')
print(set_1)

# =========================================
print(50*'=')

# Remove a random item by using the pop() method:
set_1.pop()
print(set_1)

# =========================================
print(50*'=')

# The clear() method empties the set:
set_2={'lola','sosan''sara','tawfik'}
print(set_2)
set_2.clear()
print(set_2)


# =========================================
print(50*'=')
# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}
del thisset

# will raise error
print(thisset)