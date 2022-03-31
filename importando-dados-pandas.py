import pandas as pd

# json = open('./files/aluguel.json')
# print(json)

df_json = pd.read_json('./files/aluguel.json')
print(df_json)

# txt = open('./files/aluguel.txt')
# print(txt)

# df_txt = pd.read_txt('./files/aluguel.txt')
# print(df_txt)

# df_excel = pd.read_excel('./files/aluguel.xlsx')
# print(df_excel)

# df_html = pd.read_html('./files/dados_html_1.html')
# print(df_html[0])