### === Relatório de Análise II === ###

import pandas as pd

dados = pd.read_csv('./files/aluguel.csv', sep = ';')

tipo_de_imovel = dados['Tipo']

# Tipo Pandas Series
type(tipo_de_imovel)

# print(tipo_de_imovel.drop_duplicates(inplace = True))

### === Organizando a Visualização === ###

tipo_de_imovel = pd.DataFrame(tipo_de_imovel)

# print(tipo_de_imovel.index)

# print(tipo_de_imovel.shape[0])

for i in range(tipo_de_imovel.shape[0]):
    print(i)

tipo_de_imovel.index = range(tipo_de_imovel.shape[0])
print(tipo_de_imovel)

