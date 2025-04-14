# Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

print(x.issuperset(y))
# =========================================
print(50*'=')


# Return True if all items in set x are present in set y:

x_set = {"a", "b", "c"}
y_set = {"f", "e", "d", "c", "b", "a"}

print(x_set.issubset(y_set))


# =========================================
print(50*'=')

# Return True if no items in set x is present in set y:
x_myset = {"apple", "banana", "cherry"}
y_myset = {"google", "microsoft", "facebook"}

print(x_myset.isdisjoint(y_myset))