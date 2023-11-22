import requests
import pandas as pd
import time

token ='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'

listaUsuarios = []
arrayCsv = ['../csv/split4000/CSV4000_4.csv', '../csv/split4000/CSV4000_5.csv',
            '../csv/split4000/CSV4000_6.csv', '../csv/split4000/CSV4000_7.csv',
            '../csv/split4000/CSV4000_8.csv', '../csv/split4000/CSV4000_9.csv']

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
            return 'autor nulo'
        elif data['author'].get('login') is None:
            return 'autor nulo'
        if data['commit']['author']['name'].lower() == real_name.lower():
            #print(data['author']['login'])
            return data['author']['login']
    return 'error ao obter'

def processar_csv(input_csv, output_csv):
    try:
        df_resultados = pd.read_csv(output_csv)
    except FileNotFoundError:
        df_resultados = pd.DataFrame(columns=['username', 'repositorio', 'hash', 'linguagem_programacao'])
    df_novo = pd.read_csv(input_csv)
    listaUsuarios = []

    for index, row in df_novo.iterrows():
        print(index + 1)
        username = get_username(row['repositorio'], row['autor_commit'], row['hash'])
        if username is not None:
            user = {
                'username': str(username),
                'repositorio': str(row['repositorio']),
                'hash': str(row['hash']),
                'linguagem_programacao': str(row['linguagem_programacao'])
            }
            listaUsuarios.append(user)
            print(user)
        if index % 3000 == 0 and index != 0:
            print(f"Atingido o limite de 3000 iterações. Pausando por 2 minutos...")
            time.sleep(300)

    df_resultados = pd.concat([df_resultados, pd.DataFrame(listaUsuarios)], ignore_index=True)
    df_resultados.to_csv(output_csv, index=False)

for i in arrayCsv:
    processar_csv(i, '../csv/ListagemUsernames.csv')
    time.sleep(3800)
    print('ARQUIVO FINALIZADO' + str(i))

