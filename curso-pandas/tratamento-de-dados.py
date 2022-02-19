### === Relatório de Análise V === ###
import pandas as pd

dados = pd.read_csv('./files/dados_residencial.csv', sep = ';')

# O que for nulo fica True
dados.isnull()

# O que for nulo fica Falso
dados.notnull

# dados.info()

nulos = dados[dados['Valor'].isnull()]

A = dados.shape[0]
# Removendo os valores null 
dados.dropna(subset = ['Valor'], inplace= True)
B = dados.shape[0]
print(A-B)

dados[dados['Condominio'].isnull()].shape[0]
selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())
A = dados.shape[0]
dados = dados[~selecao]
B = dados.shape[0]
print(A-B)

dados = dados.fillna({'Condominio': 0, 'IPTU': 0})

dados.info()

dados.to_csv('./files/dados_residencial.csv', sep = ';')
