import pandas as pd

dados = pd.read_csv('./curso-pandas/files/aluguel.csv', sep =';')

classes = [0, 2, 4, 6, 1000]

quartos = pd.cut(dados['Quartos'], classes)


labels = ['1 e 2 Quartos', '3 e 4 quartos', '5 e 6 quartos', '7 ou mais quartos']

quartos = pd.cut(dados['Quartos'], classes, labels = labels)
print(pd.value_counts(quartos))
