# Find a way to filter all the 's' words in a sequence
seq = ['soup', 'dog', 'salad', 'cat', 'great']

# 1st
new_seq = [x for x in seq if x[0] == 's']

# 2nd
new_seq2 = list(filter(lambda x: x[0] == 's', seq))

print(new_seq)
print(new_seq2)

