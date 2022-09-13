
import pandas as pd

df = pd.DataFrame(
    {'col1': [1, 2, 3, 4],
     'col2': [444, 555, 666, 444],
     'col3': ['abc', 'def', 'ghi', 'xyz']}
)

df.head()

data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}

df1 = pd.DataFrame(data)
