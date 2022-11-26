import requests
import json
from datetime import datetime, date, timedelta
import time
import sys


USEFULL_OWNER_KEYS = {"type", "site_admin"}
USEFULL_KEYS = {"id",
                "owner",
                "fork",
                "created_at",
                "updated_at",
                "pushed_at",
                "size",
                "stargazers_count",
                "watchers_count",
                "language",
                "has_issues",
                "has_projects",
                "has_downloads",
                "has_wiki",
                "has_pages",
                "has_discussions",
                "forks_count",
                "mirror_url",
                "archived",
                "disabled",
                "open_issues_count",
                "license",
                "allow_forking",
                "is_template",
                "web_commit_signoff_required",
                "topics",
                "default_branch",
                "permissions",
                "network_count",
                "subscribers_count"}


def get_usefull_dict(raw: dict):
    keys = list(raw.keys())
    for key in keys:
        if key not in USEFULL_KEYS:
            raw.pop(key)
    owner_keys = list(raw['owner'].keys())

    for key in owner_keys:
        if key not in USEFULL_OWNER_KEYS:
            raw['owner'].pop(key)

    return raw


def save_repos(start_date: date, end_date: date):
    DAY_INCREMENT = timedelta(days=1)
    auth = (sys.argv[1], sys.argv[2])
    tmp_date = start_date
    url = lambda _page, _date: f"https://api.github.com/search/repositories?page={_page}" \
                              f"&per_page=100&q=stars:>5+created:{str(_date)}"
    start_t = 0
    while tmp_date >= end_date:
        for page in range(1, 11):
            str_url = url(page, tmp_date)
            response = requests.get(str_url, auth=auth)
            # prev_t = start_t
            # start_t = time.time()
            if response.status_code != 200:
                # print(f"Time = {start_t-prev_t}")
                print(f"Problem: {str_url}; {response.status_code}, {response.reason}")
                # time.sleep(5)
                # if '2008-01-12' == str(tmp_date):
                #     print('svsdvdvdfavdfv')
                if response.reason == 'rate limit exceeded':
                    print(f'Rate limit exceeded for request {str_url}')
                    time.sleep((60 - datetime.today().minute + 1) * 60)
                    print('Time to wake up')
                else:
                    break
            raw = response.json()
            total_count = raw['total_count']
            repos = raw['items']

            if len(repos) == 0:
                break

            for repo in repos:
                repo_id = repo['id']
                try:
                    with open(f"data/{repo_id}.json", 'w', encoding='utf-8') as f:
                        json.dump(get_usefull_dict(repo), f, ensure_ascii=False, indent=4)
                except Exception as e:
                    print(f"id={repo_id}, url={repo['url']}", e)

            # if total_count % 100 + 1 <= page:
            #     break

        tmp_date = tmp_date - DAY_INCREMENT


if __name__ == "__main__":
    start = date(2015, 1, 1)
    end = date(2010, 1, 1)

    save_repos(start, end)
