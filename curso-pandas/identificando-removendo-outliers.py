import pandas as pd
import matplotlib as plt

dados = pd.read_csv('./curso-pandas/files/aluguel_residencial.csv', sep = ';')

dados.boxplot(['Valor'])
dados[dados['Valor'] >= 500000]

valor = dados['Valor']

# q1 = valor.quantile(.25)
# q3 = valor.quantile(.75)

# IIQ = q3 - q1
# limite_inferior = q1 - 1.5 * IIQ
# limite_superior = q3 + 1.5 * IIQ
# selecao = (valor >= limite_inferior) & (valor <= limite_superior)
# dados_new = dados[selecao]

# dados_new.boxplot(['Valor'])

grupo_tipo = dados.groupby('Tipo')['Valor']

q1 = grupo_tipo.quantile(.25)
q3 = grupo_tipo.quantile(.75)

IIQ = q3 - q1
limite_inferior = q1 - 1.5 * IIQ
limite_superior = q3 + 1.5 * IIQ

dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])

dados_new.boxplot(['Valor'], by = ['Tipo'])
