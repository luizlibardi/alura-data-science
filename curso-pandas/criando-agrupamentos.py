from tokenize import group
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('./curso-pandas/files/aluguel_residencial.csv', sep = ';')
# print(dados['Valor'].mean())
bairros = []

bairros = dados['Bairro'].unique()
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]
dados['Bairro'].drop_duplicates()
group_bairro = dados.groupby('Bairro')
# print(group_bairro.groups)

for bairro, data in group_bairro:
    print(f'{bairro} -> {data.Valor.mean()}')

print(group_bairro[['Valor', 'Condominio']].mean().round(2))


### === Estatisticas Descritivas === ###

# print(group_bairro['Valor'].describe().round(2))
# print(group_bairro['Valor'].aggregate(['min', 'max', 'sum']).rename(columns = {'min': 'mínimo', 'max': 'máximo', 'sum': 'soma'}))
plt.rc('figure', figsize = (20, 10))
fig = group_bairro['Valor'].std().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 22})
plt.show()