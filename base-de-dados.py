### === Relatório de Análise 1 === ###

import pandas as pd

dados = pd.read_csv("./files/aluguel.csv", sep = ';')

# Tipo Data Frame 
type(dados)

# head(): os 5 primeiros da DataFrame
dados.head()

### === Informações Gerais sobre a Base de Dados === ###

dados.dtypes

tipos_de_dados = pd.DataFrame(dados.dtypes, columns= ['Tipos de Dados'])
tipos_de_dados.columns.name = 'Variáveis'
# print(tipos_de_dados)

dados.shape

print(f'A base de dados apresenta {dados.shape[0]} registros e {dados.shape[1]} variáveis')