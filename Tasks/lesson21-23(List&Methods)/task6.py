friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]

del friends[0:2]

print(friends)

friends.remove('Salem')


# or you can delete by index use pop
# friends.pop(-1)

print(friends)
