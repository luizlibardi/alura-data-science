### === Relatório de Análise VI === ###

import pandas as pd

dados = pd.read_csv('./files/dados_residencial.csv', sep = ';')

dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']

dados['Valor m2'] = dados['Valor'] / dados['Area']
dados['Valor m2'] = dados['Valor m2'].round(2)

dados['Valor m2 Bruto'] = (dados['Valor Bruto'] / dados['Area']).round(2)
# print(dados.head(10))

casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')
print(dados)

