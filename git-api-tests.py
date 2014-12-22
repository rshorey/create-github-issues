import getpass
from github import GitHub

username = raw_input("Github username:")
password = getpass.getpass("Github password:")

gh = GitHub(username=username, password=password)

repo = gh.repos('rshorey')('create-github-issues')

title = "another sample issue"
body = "issue created through githubpy"

repo.issues.post(title=title, body=body)