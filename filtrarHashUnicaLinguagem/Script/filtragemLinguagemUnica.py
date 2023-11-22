import pandas as pd

# Ler o arquivo CSV com as hashes filtradas
info_filtrado = pd.read_csv('../CSVOut/info_filtrado.txt', sep='\t')

# Ler o arquivo CSV original
df_original = pd.read_csv('../CSVOut/CSVOutMarkdown.csv')

# Filtrar o DataFrame original mantendo apenas as linhas com as hashes filtradas
df_resultante = df_original[df_original['hash'].isin(info_filtrado['hash'])]

# Salvar o novo DataFrame em um novo arquivo CSV
df_resultante.to_csv('../CSVOut/CSVFiltradoUnicaLinguagem.csv', index=False)
