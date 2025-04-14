# lambda arguments : expression

c = lambda x: x + 5
print(c(7))

print(c.__name__)
print(type(c))

print('--------------')

d = lambda y, t: y * t
print(d(20, 10))

print('--------------')
my_list = [10, 20]

print(list(map(lambda f: f * 5, my_list)))
