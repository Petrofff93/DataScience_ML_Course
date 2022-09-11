# Given a nested list, use indexing to grab the word 'hello'
lst = [1, 2, [3, 4], [5, [100, 200, ["hello"]], 23, 11], 1, 7]
# 3rd index is '[5, [100, 200, ['hello']]'
# After that we have 1st idx which is '[100, 200, ['hello']'
# And finally we access the 2nd idx which is 'hello'
print(lst[3][1][2][0])
