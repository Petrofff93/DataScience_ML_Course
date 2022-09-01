import numpy as np
import pandas as pd

from numpy.random import randn

test1 = np.random.seed(101)
data_frame = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

df_test = data_frame['W']
