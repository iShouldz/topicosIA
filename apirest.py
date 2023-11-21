import requests

CONTA2 = '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'
TOKEN = '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'

url = 'https://api.github.com/users/iShouldz/orgs'
headers = {'Authorization': f'token {TOKEN}'}

response = requests.head(url, headers=headers)

# Extraindo os cabeçalhos da resposta
headers = response.headers

# Imprimindo os cabeçalhos específicos de interesse
print("HTTP Status:", response.status_code)
print("Rate Limit Limit:", headers.get('x-ratelimit-limit'))
print("Rate Limit Remaining:", headers.get('x-ratelimit-remaining'))
print("Rate Limit Reset:", headers.get('x-ratelimit-reset'))
