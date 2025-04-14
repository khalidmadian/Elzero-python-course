
# The conditional expression (x if x != "kiwi" else "orange") is part of the value being added to the new list,
# so it must come before the for loop.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

toto_list = [x if x != "kiwi" else "orange" for x in fruits if x != "mango"]

print(toto_list)

# l = [ expression for item in iterable if condition]