import pandas as pd
import requests

token = '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'

def getLinhasTotais(repository_url, commit_hash):
    user, repo = repository_url.split('/')[-2:]
    api_url = f"https://api.github.com/repos/{user}/{repo}/commits/{commit_hash}"
    print(api_url)

    headers = {
        'Authorization': f'token {token}',
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        linhasAdicionadas = data['stats']['total']
        print('Total de linhas do commit: ' + str(data['stats']['total'])+'\n*Deleções e adições incluídas*')
        return linhasAdicionadas
    return None

# Função para ler o arquivo CSV, adicionar uma nova coluna e salvar o CSV modificado
def processar_csv(input_csv, output_csv):
    # Ler o CSV para um DataFrame do pandas
    df = pd.read_csv(input_csv)

    # Adicionar uma nova coluna chamada 'LinhasAdicionadas'
    df['LinhasAdicionadas'] = df.apply(lambda row: getLinhasTotais(row['repositorio'], row['hash']), axis=1)

    # Salvar o DataFrame modificado de volta ao CSV
    df.to_csv(output_csv, index=False)

# Exemplo de uso
input_csv_path = 'csv/split/output_chunk_1.csv'
output_csv_path = 'csv/hashWithTotal.csv'
processar_csv(input_csv_path, output_csv_path)
