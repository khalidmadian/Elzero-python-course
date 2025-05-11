set1 = {'hi', True, 50, 'hi'}
set2 = {'one', 'two', 'three'}
myset = {"a", "b", "c"}

set3 = set1 | set2 | myset

print(set3)

# =========================================
print(50 * '=')
# The union() and update() methods joins all items from both sets.


set4 = set1.union(set2, myset)
print(set4)

# The update() changes the original set, and does not return a new set.
set2.update(myset)
print(set2)

# =========================================
print(50 * '=')
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# You can use the & operator instead of the intersection() method, and you will get the same result.

my_set1 = {"apple", "banana", "cherry"}
my_set2 = {"google", "microsoft", "apple"}

my_set3 = my_set1.intersection(my_set2)
my_set4 = my_set1 & my_set2
print(my_set3)
print(my_set4)

# =========================================
print(50 * '=')
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

my_set1.intersection_update(my_set2)
print(my_set1)


# =========================================
print(50 * '=')
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# You can use the - operator instead of the difference() method, and you will get the same result.

hi_set1 = {"apple", "banana", "cherry"}
hi_set2 = {"google", "microsoft", "apple"}

hi_set3=hi_set1.difference(hi_set2)
print(hi_set1-hi_set2)
print(hi_set3)

# =========================================
print(50 * '=')
# The difference_update() method will also keep the items from the first set that are not in the other set,
# but it will change the original set instead of returning a new set.

hi_set1.difference_update(hi_set2)
print(hi_set1)


# =========================================
print(50 * '=')
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

sy_set1 = {"apple", "banana", "cherry"}
sy_set2 = {"google", "microsoft", "apple"}

sy_set3=sy_set1.symmetric_difference(sy_set2)
print(sy_set1^sy_set2)
print(sy_set3)

# =========================================
print(50 * '=')
# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

sy_u_set1 = {"apple", "banana", "cherry"}
sy_u_set2 = {"google", "microsoft", "apple"}

sy_u_set1.symmetric_difference_update(sy_u_set2)
print(sy_u_set1)