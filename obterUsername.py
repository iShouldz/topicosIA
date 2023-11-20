import requests

def get_username(repository_url, real_name, commit_hash):
    user, repo = repository_url.split('/')[-2:]

    api_url = f"https://api.github.com/repos/{user}/{repo}/commits/{commit_hash}"
    print(api_url)
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        print(data['committer']['login'])
        if data['commit']['author']['name'].lower() == real_name.lower():
            print(data['author']['login'])
            return data['author']['login']
    return 'error ao obter'

username = get_username('https://github.com/bminor/glibc', 'Ulrich Drepper', '2864e767053317538feafa815046fff89e5a16be')
print(username)
