import os
import requests
import json

def close_issues_with_ids(repo, access_token, issue_numbers):
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    for issue_number in issue_numbers:
        url = f'https://api.github.com/repos/{repo}/issues/{issue_number}'
        data = {'state': 'closed'}
        response = requests.patch(url, json=data, headers=headers)

        if response.status_code == 200:
            print(f"Issue {issue_number} closed successfully.")
        else:
            print(f"Failed to close issue {issue_number}. Status code: {response.status_code}")

issues_ids = json.loads(os.environ["ISSUES_ID"])
repo = os.environ["REPO"]
access_token = os.environ["GH_TOKEN"]
if issues_ids:
    close_issues_with_ids(repo, access_token, issues_ids)
else:
    print("There are no regresion issues with the title")