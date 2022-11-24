import requests
import json
import time

since = 0
url = "https://api.github.com/repositories?since="
start = time.time()

for i in range(10000):
    resp = requests.get(url + str(since))
    if resp.status_code != 200:
        print(f"Status code: {resp.status_code}, iter={i}, time={time.time()-start}")
    repos_json = resp.json()
    since = repos_json[-1]['id']

    for repo in repos_json:
        repo_id = repo['id']
        with open(f"data/{repo_id}.json", 'w') as f:
            json.dump(repo, f, indent=4)
        # with open(f"data/{repo_id}.json", 'w', encoding='utf-8') as f:
        #     json.dump(repo, f, ensure_ascii=False, indent=4)
    if i % 10:
        print(f"Saved: {i*100} repos")



