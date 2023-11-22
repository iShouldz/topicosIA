import pandas as pd

# Ler o arquivo de texto com as informações
info_por_hash = pd.read_csv('../CSVOut/info_por_hash.txt', sep='\t')

# Filtrar as linhas onde a quantidade de linguagens é igual a 1
info_filtrado = info_por_hash[info_por_hash['quantidade_linguagens'] == 1]

# Salvar o novo DataFrame em um novo arquivo de texto
info_filtrado.to_csv('../CSVOut/info_filtrado.txt', index=False, sep='\t')
