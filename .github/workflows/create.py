from github import Github
import os
import sys

token = os.getenv('GITHUB_TOKEN', str(sys.argv[1]))
g = Github(token)
repo = g.get_repo("jhu-covid-devops/COVID-19")

branch_name = str(sys.argv[2]) + '_' + str(sys.argv[3])
branch_name = branch_name.replace(" ","_")

source = repo.get_branch("master")
repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=source.commit.sha)
