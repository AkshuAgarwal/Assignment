"""
A list stores three dictionaries each storing details (old price, new price, change). Write a Python program to
create a DataFrame from it.
"""

import pandas as pd

data = [{"Old Price": 7800}, {"New Price": 8000}, {"Change": 200}]

df = pd.DataFrame(data)
print(df)
