def test_repeat(word):  # wwooorrlllddd
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return test_repeat(word[1:])

    return word[0] + test_repeat(word[1:])


print(test_repeat('wwooorrlllddd'))
