import os
import requests

REPO = os.environ["REPO"]
GH_TOKEN = os.environ["GH_TOKEN"]

def get_issue_ids_by_title(repo, title):
    
    headers = {
        'Authorization': f'token {GH_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    
    params = {
        'q': f'repo:{repo} is:issue is:open in:title "{title}"'
    }
    
    url = 'https://api.github.com/search/issues'
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data)

    if 'items' in data:
        return [issue['id'] for issue in data['items']]
    else:
        return []
    
def delete_issues_by_id(issue_id):
    print("id:", issue_id)
    url = f"https://api.github.com/repos/{REPO}/issues/{issue_id}"
    headers = {
        "Authorization": f"token {GH_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        'X-GitHub-Api-Version': '2022-11-28',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        '{"state":"closed"}'
    }
    print(requests.get(url, headers=headers))

    response = requests.patch(url, headers=headers, data=data)
    
    if response.status_code == 200:
        print(f"Issue {issue_id} closed successfully.")
    elif response.status_code == 404:
        print(f"Issue {issue_id} not found.")
    else:
        print(f"Failed to close issue {issue_id}. Status code: {response.status_code}")
        print(response.text)

def get_issue(issue_id):
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'token {GH_TOKEN}',
    'X-GitHub-Api-Version': '2022-11-28',
    }

    response = requests.get(f'https://api.github.com/repos/issues/{issue_id}', headers=headers)
    data = response.json()
    print(data)

issue_title = 'Test issue'

issue_ids = get_issue_ids_by_title(REPO, issue_title)
print("Issue IDs:", issue_ids)
for issue_id in issue_ids:
    get_issue(issue_id)
