import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('../../csv/ListagemUsernames.csv')

# Contar o número de linguagens diferentes para cada hash
contagem_por_hash = df.groupby('hash')['linguagem_programacao'].nunique()

# Criar um DataFrame com as informações
info_por_hash = pd.DataFrame({'hash': contagem_por_hash.index, 'quantidade_linguagens': contagem_por_hash.values})

# Salvar as informações em um arquivo de texto
info_por_hash.to_csv('info_por_hash.txt', index=False, sep='\t')

