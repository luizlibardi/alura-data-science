import pandas as pd


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

df = pd.DataFrame(data, list('321'), list('ZYX'))
df.sort_index(inplace= True)
df.sort_index(inplace= True, axis = 1)
# print(df)

df.sort_values(by= 'X', inplace= True)
print(df)