import pandas as pd


data = [
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 15, 16)
    ]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())


print(df[1:3])
print(df.loc[['l3', 'l2']])
print(df.iloc[[2, 0], [3, 0]])

