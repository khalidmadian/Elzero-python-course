my_tuple_1=('khalid','ahmed','saad','khalid')
my_tuple_2=('one',23,True)


# will raise an error cant change or edit on tuple
# my_tuple_2[1]='dddd'
# my_tuple_2.append('noha')

#try
my_tuple_1_to_list=list(my_tuple_1)
print(type(my_tuple_1_to_list))

my_tuple_1_to_list.append('mona')

my_tuple_1=tuple(my_tuple_1_to_list)


print(my_tuple_1)



