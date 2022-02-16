### === Series === ###

import pandas as pd

data = [1, 2, 3, 4, 5]

s = pd.Series(data)
# print(s)

index = ['Linha' + str(i) for i in range(5)]
# print(index)

s = pd.Series(data = data, index = index)
# print(s)

data = {'Linha' + str(i) : i + 1 for i in range(5)}
# print(data)

s = pd.Series(data)
# print(s)

# Soma 2 em cada numero de s
s1 = s + 2
# print(s1)

### === Data Frame === ###

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(data)

index = ['Linha ' + str(i) for i in range(3)]
columns = ['Coluna ' + str(i) for i in range(3)]


df1 = pd.DataFrame(data = data, index = index, columns=columns)
df2 = df1
df3 = df1

df1[df1 > 0] = 'A'
df2[df2 > 0] = 'B'
df3[df3 > 0] = 'C'

df4 = pd.concat([df1, df2, df3], axis= 1)
print(df4)




