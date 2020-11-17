from github import Github
import os
import sys

token = os.getenv('GITHUB_TOKEN', str(sys.argv[1]))
g = Github(token)
repo = g.get_repo("jhu-covid-devops/COVID-19")
issues = repo.get_issues(state="open")

branch_name = str(issues.get_page(0)[0].title).replace(" ","_")
# branch_name = str(sys.argv[2]).replace(" ","_")

source = repo.get_branch("master")
repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=source.commit.sha)
