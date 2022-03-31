### === Relatório de Análises IV === ###

## Tasks ##
# 1) Selecione somente os imóveis classificados com tipo 'Apartamento'
# 2) Selecione os imóveis classificados com tipos 'Casa', 'Casa de condomínio' e 'Casa de Vila'
# 3) Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites 
# 4) Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00

import pandas as pd

dados = pd.read_csv("./files/dados_residencial.csv", sep = ';')

# 1)
selecao = dados['Tipo'] == 'Apartamento' # Selecionando somente os tipo Apartamento
n1 = dados[selecao].shape[0] # Verificando a quantidade de Imóveis Apartamentos com shape
print(f"Existem {n1} imóveis classificados com tipo 'Apartamento'")
# 2)
selecao2 = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
n2 = dados[selecao2].shape[0] 
print(f"Existem {n2} imóveis classificados com tipo 'Casa', 'Casa de condomínio' e 'Casa de Vila'")

# 3)
selecao3 = (dados['Area'] >=60) & (dados['Area'] <=100)
n3 = dados[selecao3].shape[0] 
print(f"Existem {n3} imóveis com área entre 60 e 100 metros quadrados, incluindo os limites")

#4)
selecao4 = (dados['Quartos'] >=4) & (dados['Valor'] < 2000)
n4 = dados[selecao4].shape[0] 
print(f"Existem {n4} imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00")
