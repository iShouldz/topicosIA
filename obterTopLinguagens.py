import requests
#Com base nos bytes de codigo

token = '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'

username = 'Erro'

url = f'https://api.github.com/users/{username}/repos'
headers = {
    'Authorization': f'token {token}'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    repositories = response.json()
    languages_count = {}

    for repo in repositories:
        languages_url = repo['languages_url']
        response_languages = requests.get(languages_url, headers=headers)
        languages_data = response_languages.json()

        for language, bytes_of_code in languages_data.items():
            if language in languages_count:
                languages_count[language] += bytes_of_code
            else:
                languages_count[language] = bytes_of_code

    # Obtém as 3 linguagens mais usadas
    most_used_languages = sorted(languages_count.items(), key=lambda x: x[1], reverse=True)[:3]

    print(f"As 3 linguagens mais usadas por {username} são:")
    for language, bytes_of_code in most_used_languages:
        print(f"{language}: {bytes_of_code} bytes de código")

else:
    print(f"Erro ao obter os repositórios. Código de status: {response.status_code}")
