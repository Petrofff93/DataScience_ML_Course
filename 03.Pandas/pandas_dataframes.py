import numpy as np
import pandas as pd

from numpy.random import randn

test1 = np.random.seed(101)
data_frame = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

df_test = data_frame['W']

p = [a * b for a in [2, 4, 6, 8] for b in [1, 3, 5]]

labels = ['a', 'b', 'c']
my_d = [10, 20, 30]
arr = np.array(my_d)
d = {'a': 10, 'b': 20, 'c': 30}

pd.Series(data=my_d)
ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
ser3 = pd.Series(data=labels)

seed = np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
