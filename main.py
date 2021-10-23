from jira.client import JIRA
from requests.auth import HTTPBasicAuth
import requests
import json
from JiraUserDto import JiraUserDto

jira_server_raw = "https://decode.atlassian.net"
jira_user = "" # your.email@decode.agency
jira_password = "" # your jira password
jira_api_token = "" #
"""
[JIRA web page] -> profile -> Account settings -> Security -> Create and manage API tokens
Generiras token i zaljepis iznad
"""

jira_server = {'server': jira_server_raw}
jira = JIRA(options=jira_server, basic_auth=(jira_user, jira_api_token))

# primjer
issue = jira.issue("IDTR-153")

auth = HTTPBasicAuth(jira_user, jira_api_token)
headers = {
    "Accept": "application/json"
}
meUrl = "{}/rest/api/3/myself".format(jira_server_raw)
print(meUrl)
response = requests.request(
    "GET",
    meUrl,
    headers=headers,
    auth=auth
)

jiraUser = JiraUserDto().serialize(json.dumps(json.loads(response.text)), True)
print(jiraUser.accountId)
#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

#issues2 = jira.search_issues('assignee = currentUser()')
#print(issues2)

issueListUrl = "{}/rest/api/3/search".format(jira_server_raw)

query = {
    'jql': 'assignee in ({})'.format(jiraUser.accountId),
    'maxResults': 2,
    'fieldsByKeys': False,
    'fields': [
        'reporter',
        'status',
        'assignee',
        'project'
    ],
    'startAt': 0
}

response = requests.request(
    "GET",
    issueListUrl,
    headers=headers,
    params=query,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

# ovo radi, al pokusavam sad trenutno isto preko v3 dohvatiti issue
#jqlCustom = "assignee in ({})".format(jiraUser.accountId)
#issues = jira.search_issues(jqlCustom)
#print(issues)





if __name__ == '__main__':
    pass
    #print("Test")
