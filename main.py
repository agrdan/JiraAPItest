from jira.client import JIRA

jira_server = "https://decode.atlassian.net"
jira_user = "" # your.email@decode.agency
jira_password = "" # your jira password
jira_api_token = "" #
"""
[JIRA web page] -> profile -> Account settings -> Security -> Create and manage API tokens
Generiras token i zaljepis iznad
"""

jira_server = {'server': jira_server}
jira = JIRA(options=jira_server, basic_auth=(jira_user, jira_api_token))

# primjer
# issue = jira.issue("IDTR-154")
# print(issue.fields.description)
# worklog = issue.field.worklog




if __name__ == '__main__':
    print("Test")
