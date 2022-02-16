### === Relatório de analise III === ###

# Imóveis Residenciais

import pandas as pd

dados = pd.read_csv('./files/aluguel.csv', sep = ';')
dados.head(10)

list(dados['Tipo'].drop_duplicates())

residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']

selecao = dados['Tipo'].isin(residencial)

dados_residencial = dados[selecao]

list(dados_residencial['Tipo'].drop_duplicates())
dados_residencial.shape[0]

dados_residencial.index = range(dados_residencial.shape[0])
print(dados_residencial)


### === Exportando a Base de Dados === ###

dados_residencial.to_csv('./files/dados_residencial.csv', sep = ';', index = False)
print(pd.read_csv('./files/dados_residencial.csv', sep = ';'))