nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}

merge_1 = nums | letters
print(merge_1)

print(50 * '=')

merge_2 = nums.union(letters)
print(merge_2)

print(50 * '=')

nums.update(letters)
print(nums)
