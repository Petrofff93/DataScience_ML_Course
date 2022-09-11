"""
Create a function that counts the number of times the word “dog” occurs in a string. Again ignore edge cases.
"""


def count_dog(example):
    # this is the fastest way (at least the fastest i know)
    # We could solve this with for 'loop and counter'
    splitted = example.split()
    return splitted.count("dog")


test_str = "This dog runs faster than the other dog dude!"
print(count_dog(test_str))
