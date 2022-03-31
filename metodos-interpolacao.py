import pandas as pd

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)
print(s)

# Preenchendo valores Nulos com um valor específico
print(s.fillna(0))

# Preenchendo valores Nulos com o valor anterior (de cima).
print(s.fillna(method= 'ffill'))

# Preenchendo valores Nulos com o valor de média.
print(s.fillna(s.mean()))

# Preenchendo valores Nulos com o valor anterior apenas uma vez (limite 1).
print(s.fillna(method= 'ffill', limit= 1))

# Preenchendo valores Nulos com o valor posterior (de baixo) e limite 1.
print(s.fillna(method= 'bfill', limit= 1))

