thisdict = {
    "brand": ["Ford",'chevrolet'],
    "model": "Mustang",
    "year": 1964
}

print(thisdict["brand"])

# =========================================
print(50 * '=')
# There is also a method called get() that will give you the same result:

x = thisdict.get('brand')[0]
print(x)

# =========================================
print(50 * '=')
# The keys() method will return a list of all the keys in the dictionary.
# note: keys() takes no argument
print(thisdict.keys())
thisdict['color'] = 'red'
print(thisdict.keys())

# =========================================
print(50 * '=')
# The values() method will return a list of all the values in the dictionary.
# note: values() takes no argument

print(thisdict.values())

# =========================================
print(50 * '=')
# The items() method will return each item in a dictionary, as tuples in a list

print(thisdict.items())

# =========================================
print(50 * '=')
# To determine if a specified key is present in a dictionary use the in keyword:
if 'model' in thisdict:
    print('yes this word is included')

# =========================================
print(50 * '=')
# You can change the value of a specific item by referring to its key name:

print(thisdict)
thisdict['color'] = 'blue'
print(thisdict)

# =========================================
print(50 * '=')
# The update() method will update the dictionary with the items from the given argument.

print(thisdict)
thisdict.update({'color':'black','model':'explorer'})
print(thisdict)

# =========================================
print(50 * '=')
# The popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)

# =========================================
print(50 * '=')
# The clear() method empties the dictionary:

thisdict.clear()
print(thisdict)



# =========================================
print(50 * '=')
# The del keyword removes the item with the specified key name:
del thisdict
# print(thisdict)  will raise error this dict is not defined

