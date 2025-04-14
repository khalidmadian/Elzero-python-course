from libfuturize.fixes.fix_execfile import expression

# list comprehension syntax
# l = [ expression for item in iterable if condition]



this_list = ["apple", "banana", "cherry"]

tropical = ["mango", "pineapple", "papaya"]

my_list = [x for x in this_list if "a" in x]

toto = [x for x in tropical if x != "papaya"]

print(my_list)

print(toto)
