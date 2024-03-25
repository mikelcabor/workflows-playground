import os
import requests

def get_repo_issues(repo, access_token):
    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    
    url = f'https://api.github.com/repos/{repo}/issues'
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def get_issue_ids_by_title(response_data, title):
    filtered_items = [item for item in response_data if item.get('title') == title]
    ids = []
    for item in filtered_items:
        ids.append(item['number'])
    return ids

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

# Example usage
repo = os.environ["REPO"]
access_token = os.environ["GH_TOKEN"]
title = "Test issue"

repo_issues = get_repo_issues(repo, access_token)
issue_ids = get_issue_ids_by_title(repo_issues, title)
print(issue_ids)
#if issue_ids:
#    close_issues_with_ids(repo, access_token, issue_ids)
#else:
#    print("There are no issues with the title: ", title)