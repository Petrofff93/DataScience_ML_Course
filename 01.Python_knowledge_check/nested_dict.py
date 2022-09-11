# Given this nested dictionary grab the word “hello”. Be prepared, this will be annoying/tricky
d = {
    "k1": [
        1,
        2,
        3,
        {"tricky": ["oh", "man", "inception", {"target": [1, 2, 3, "hello"]}]},
    ]
}

"""
First we are accessing the 3rd idx of the value of 'k1' key.
The result is '{'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}'.
After that we have a new key with nested values - we have to call the 'tricky' key with 3rd idx value.
Then we have access to '{'target': [1, 2, 3, 'hello']'.
We have to access the 'target' key and the value which stands on the 3rd idx (the 'hello' word)

"""
print(d["k1"][3]["tricky"][3]["target"][3])
