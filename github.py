import requests

print('GitHub Users\n')

username = input('Enter username\n')

url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    # print(data)
    print(f'\nNome: {data["login"]}')
    print(f'Seguidores: {data["followers"]}')
    print(f'Seguindo: {data["following"]}')
    print(f'Repos: {data["public_repos"]}')
    print(f'Repos_url: {data["repos_url"]}')
else:
    print('Failed to user')