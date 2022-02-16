import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importando um csv com pandas
notas = pd.read_csv("./files/ratings.csv")
# .columns para mudar o nome das colunas
notas.columns = ["usuarioID", "filmeID", "nota", "momento"]

## Series

# .head() Para exibir os 5 primeiros (do 0 ao 4)
cinco_primeiras = notas.head()
# print(cinco_primeiras)



# print(notas)

# Valores Unicos
notas_unicas = notas['nota'].unique()
# print(notas_unicas)

# Contar valores
contar_valores = notas['nota'].value_counts()
# print(contar_valores)

# Media dos valores 
media = notas['nota'].mean()
# print(media)

# Mediana dos valores
mediana = notas['nota'].median()
# print(mediana)

# print(notas.nota.plot(kind='hist'))

# .describe para Descrever
descricao_notas = notas.nota.describe()
# print(descricao_notas)

# sns.boxplot(notas.nota)

# Importando um csv com pandas
filmes = pd.read_csv("./files/movies.csv")
# .columns para mudar o nome das colunas
filmes.columns = ["filmeID", "titulo", "generos"]
# print(filmes.head())
 
# Notas em Geral
notas_em_geral = notas.query("filmeID==1").nota
# print(notas_em_geral)

# Analisando media de notas especificas por filme
notas_por_filme = notas.query("filmeID==1").nota.mean()
# print(notas_por_filme)

# Agrupando notas por grupo
medias_por_filme = notas.groupby("filmeID").mean()["nota"]
# print(medias_por_filme.describe())

plt.title("Histograma da media por filme")
# print(plt.hist(medias_por_filme))


# Importando um csv com pandas
filmes_tmdb = pd.read_csv("./files/tmdb_movies.csv")
# print(filmes_tmdb.head())

todas_as_linguas = filmes_tmdb.original_language.unique()
# print(todas_as_linguas)

# Contando quantas vezes cada lingua aparece
contagem_linguas = filmes_tmdb["original_language"].value_counts()

# Utilizando .columns para mudar o nome das colunas
contagem_linguas.columns = ["original_language", "total"]
# print(contagem_linguas.head())

# plt.pie(contagem_linguas["total"], labels = contagem_linguas["original_language"])

total_contagem_linguas = contagem_linguas.sum()
contagem_ingles = contagem_linguas.loc["en"]
total_resto = (total_contagem_linguas - contagem_ingles)
# print(contagem_ingles, total_resto)

## Criando dataframe para visualizar as linguas
dados = {
    'lingua' : ['ingles', 'outros'],
    'total': [contagem_ingles, total_resto]
}

dados = pd.DataFrame(dados)
# print(dados)

so_ingles = filmes_tmdb.query("original_language == 'en'")
total_outras_linguas = filmes_tmdb.query("original_language != 'en'").value_counts()
# print(total_outras_linguas)

notas_toy_story = notas.query("filmeID==1")
notas_jumanji = notas.query("filmeID==2")
# print(len(notas_toy_story), len(notas_jumanji))

# print("Nota média do Toy Story %.2f" % notas_toy_story.nota.mean())
# print("Nota média do Jumanji %.2f" % notas_jumanji.nota.mean())

filme1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10))
filme2 = np.append(np.array([5] * 10), np.array([1] * 10))

print(filme1.mean(), filme2.mean())
print(filme1.median(), filme2.median())

