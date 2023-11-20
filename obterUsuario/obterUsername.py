import requests
import pandas as pd
import time

token = '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'
listaUsuarios = []

def get_username(repository_url, real_name, commit_hash):
    user, repo = repository_url.split('/')[-2:]

    api_url = f"https://api.github.com/repos/{user}/{repo}/commits/{commit_hash}"
    print(api_url)
    headers = {
        'Authorization': f'token {token}'
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        if data['author'] is None:
            return None
        if data['commit']['author']['name'].lower() == real_name.lower():
            if data['author']['login'] is None:
                return 'erro ao obter'
            else:
                #print(data['author']['login'])
                return data['author']['login']
    return 'error ao obter'

def processar_csv(input_csv):
    df = pd.read_csv(input_csv)
    listaUsuarios = []

    for index, row in df.iterrows():
        username = get_username(row['repositorio'], row['autor_commit'], row['hash'])
        if username is not None:
            #and username not in listaUsuarios
            user = str(username) + 'repo[' + str(row['repositorio']) + ']' + str(row['hash']) \
                   + str(row['linguagem_programacao'])
            listaUsuarios.append(user)

        if index % 1000 == 0 and index != 0:
            print(f"Atingido o limite de 100 iterações. Pausando por 3 minutos...")
            time.sleep(180)

    with open('../obterUsuario/listaUsernamesCommits.txt', 'w') as arquivo:
        for item in listaUsuarios:
            arquivo.write(f"{item}\n")
    #df.to_csv('resultados.csv', index=False)

input_csv_path = '../csv/hashRepoURL.csv'
processar_csv(input_csv_path)
