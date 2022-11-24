import requests
import json

# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
url1 = 'https://api.github.com/search/repositories?q=java&page=3&per_page=150'
url2 = "https://api.github.com/repositories?since=367"
resp1 = requests.get(url1)
resp2 = requests.get(url2)
print(resp1.status_code, resp2.status_code)
resp1 = resp1.json()['items']
resp2 = resp2.json()
# print(len(resp1[0]), len(resp2[0]), len(set(resp1[0]) & set(resp2[0])))
# print(set(resp1[0]) & set(resp2[0]))

# print(resp_dict.keys())

i = 0

for repository in resp1:
# for i, repository in enumerate(resp_dict):
    i += 1
    name = repository["full_name"]
    print(f"{i}\t{name}\t\tid={repository['id']}")
    # language = 'l'