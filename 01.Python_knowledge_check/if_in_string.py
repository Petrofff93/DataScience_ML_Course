"""
Create a basic function that returns True if the word ‘dog’ is contained in the input string.
Don’t worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
"""


def find_dog(example):
    for item in example.split():
        if item == "dog":
            return True
    return False


test_str = "Is there a dog here?"
print(find_dog(test_str))
