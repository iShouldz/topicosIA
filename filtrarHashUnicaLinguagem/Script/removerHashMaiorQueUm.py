import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('../../csv/ListagemUsernames.csv')

# Contar o número de linguagens diferentes para cada hash
contagem_por_hash = df.groupby('hash')['linguagem_programacao'].nunique()

# Filtrar hashes com quantidade de linguagens igual a 1
hashes_com_uma_linguagem = contagem_por_hash[contagem_por_hash == 1].index

# Filtrar o DataFrame original
df_filtrado = df[df['hash'].isin(hashes_com_uma_linguagem)]

# Salvar o novo DataFrame em um novo arquivo CSV
df_filtrado.to_csv('hashUnicoCommit.csv', index=False)
