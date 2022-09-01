import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)

d = {
    'a': 10,
    'b': 20,
    'c': 30
}

# Using the two lists my_data and labels
series_test = pd.Series(data=my_data, index=labels)
# Using the numpy array and labels as index
series_test2 = pd.Series(data=arr, index=labels)
# Using the dictionary
series_test3 = pd.Series(d)

# Test with only labels
series_test4 = pd.Series(labels)

# We can pass built-in functions as a data param. It will return the references
series_test5 = pd.Series(data=[sum, print, len])

series_test6 = pd.Series([1, 2, 3, 4], ['USA', 'Deutschland', 'Poland', 'Bulgaria'])
series_test7 = pd.Series([1, 2, 5, 4], ['USA', 'Italy', 'Japan', 'China'])

# Try to add two series
series_test8 = series_test6 + series_test7
