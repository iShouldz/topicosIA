import pandas as pd
import requests

token = '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'

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

            return 'Erro'
        if data['commit']['author']['name'].lower() == real_name.lower():
            if data['author']['login'] is None:
                return 'erro ao obter'
            else:
                print(data['author']['login'])
                return data['author']['login']
    return 'error ao obter'


def obter_linguagens_mais_utilizadas(username):
    url = f'https://api.github.com/users/{username}/repos'
    headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repositorios = response.json()

        linguagens = {}
        for repositorio in repositorios:
            stats_url = f'https://api.github.com/repos/{username}/{repositorio["name"]}/languages'
            stats_response = requests.get(stats_url, headers=headers)

            if stats_response.status_code == 200:
                stats = stats_response.json()
                for linguagem, contagem in stats.items():
                    linguagens[linguagem] = linguagens.get(linguagem, 0) + contagem
        linguagens_mais_utilizadas = sorted(linguagens.items(), key=lambda x: x[1], reverse=True)[:3]

        return linguagens_mais_utilizadas
    else:
        print(f'Erro ao obter repositórios. Código de resposta: {response.status_code}')
        return None

def verificar_linguagem(usuario, linguagem):
    linguagens_mais_utilizadas = obter_linguagens_mais_utilizadas(usuario)
    print(linguagens_mais_utilizadas)

    return linguagem in [lang[0] for lang in linguagens_mais_utilizadas]

def processar_csv(input_csv):
    df = pd.read_csv(input_csv)
    positivos = []
    negativos = []

    for index, row in df.iterrows():
        username = get_username(row['repositorio'], row['autor_commit'], row['hash'])

        if username:
            if verificar_linguagem(username, row['linguagem_programacao']):
                positivos.append(1)
                negativos.append(0)
            else:
                positivos.append(0)
                negativos.append(1)
        else:
            positivos.append(0)
            negativos.append(0)

    df['Positivo'] = positivos
    df['Negativo'] = negativos

    df.to_csv('resultados.csv', index=False)

input_csv_path = 'csv/split300/output_chunk_1.csv'
processar_csv(input_csv_path)
