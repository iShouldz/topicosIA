import requests
import pandas as pd
import time

token = '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'
token2 = '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'

conta2 = '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'
listaUsuarios = []
arrayCsv = ['../csv/split5000/CSV5000.csv_1.csv', '../csv/split5000/CSV5000.csv_2.csv',
            '../csv/split5000/CSV5000.csv_3.csv', '../csv/split5000/CSV5000.csv_4.csv',
            '../csv/split5000/CSV5000.csv_5.csv', '../csv/split5000/CSV5000.csv_6.csv',
            '../csv/split5000/CSV5000.csv_7.csv', '../csv/split5000/CSV5000.csv_8.csv']

def get_username(repository_url, real_name, commit_hash):
    user, repo = repository_url.split('/')[-2:]

    api_url = f"https://api.github.com/repos/{user}/{repo}/commits/{commit_hash}"
    print(api_url)
    headers = {
        'Authorization': f'token {token}'
    }
    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        if data['author'] is None:
            return None
        if data['commit']['author']['name'].lower() == real_name.lower():
            #print(data['author']['login'])
            return data['author']['login']
    return 'error ao obter'

def processar_csv(input_csv, output_csv):
    try:
        # Tenta ler o arquivo CSV existente
        df_resultados = pd.read_csv(output_csv)
    except FileNotFoundError:
        # Se o arquivo não existir, cria um DataFrame vazio
        df_resultados = pd.DataFrame(columns=['username', 'repositorio', 'hash', 'linguagem_programacao'])
    df_novo = pd.read_csv(input_csv)
    listaUsuarios = []

    for index, row in df_novo.iterrows():
        print(index)
        username = get_username(row['repositorio'], row['autor_commit'], row['hash'])
        if username is not None:
            user = {
                'username': str(username),
                'repositorio': str(row['repositorio']),
                'hash': str(row['hash']),
                'linguagem_programacao': str(row['linguagem_programacao'])
            }
            listaUsuarios.append(user)
            #print(user)
        if index % 3000 == 0 and index != 0:
            print(f"Atingido o limite de 3000 iterações. Pausando por 2 minutos...")
            time.sleep(120)

    df_resultados = pd.concat([df_resultados, pd.DataFrame(listaUsuarios)], ignore_index=True)
    df_resultados.to_csv(output_csv, index=False)

processar_csv('../csv/split4000/CSV4000_1.csv', '../csv/ListagemUsernames.csv')


