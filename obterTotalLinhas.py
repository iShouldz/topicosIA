import requests

def getLinhasTotais(repository_url, commit_hash):
    user, repo = repository_url.split('/')[-2:]
    api_url = f"https://api.github.com/repos/{user}/{repo}/commits/{commit_hash}"
    print(api_url)
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        linhasAdicionadas = data['stats']['total']
        print('Total de linhas do commit: ' + str(data['stats']['total'])+'\n*Deleções e adições incluidas*')
    return None

print(getLinhasTotais('https://github.com/bminor/glibc', '2864e767053317538feafa815046fff89e5a16be'))
