import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('../../csv/ListagemUsernames.csv')

# Filtrar as linhas que não contêm 'Markdown' na coluna 'linguagem_programacao'
df_filtrado = df[df['linguagem_programacao'] != 'Markdown']

# Salvar o novo DataFrame em um novo arquivo CSV
df_filtrado.to_csv('CSVOutMarkdown.csv', index=False)
