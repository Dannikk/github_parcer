from github import Github
import json
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


def save_repos(g):
    i = 0
    for repo in g.get_repos(since=0):
        i += 1
        id = repo.id
        try:
            with open(f"pgh_data/{id}.json", 'w', encoding='utf-8') as f:
                json.dump(get_usefull_dict(repo.raw_data), f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"i={i}, id={id}, url={repo.url}", e)
        if i % 100 == 0:
            print(f"Saved {i} repos")
        if i > 500_000:
            print(f"Good job, buddy!\n\tLast repo's id={id}")


if __name__ == "__main__":
    token = sys.argv[1]
    g = Github(token)
    save_repos(g)
