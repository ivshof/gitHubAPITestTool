# Test tool to check git hub commit changes

import sys
import logging
from github import Github
import os
from pprint import pprint

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(message)s')





def main():

    envPossibleValues = ['dev', 'sit', 'qa', 'prod']

    # Ensure correct usage of input parameters
    if len(sys.argv) < 4 or len(sys.argv) > 6:
        logging.info("Input parameters ERROR")
        sys.exit("Usage: python git-test.py repo apiToken environment {commitHash}")

    elif len(sys.argv) == 4:
        commitHash = "none"

    elif len(sys.argv) == 5:
        commitHash = str(sys.argv[4])

    repoValue = str(sys.argv[1])
    apiToken = str(sys.argv[2])
    environment = str(sys.argv[3])


    # Check if environment is in list of possible values
    if environment not in envPossibleValues:
        logging.info("Input environment value ERROR")
        sys.exit("Usage: 'environment' possible values: dev, sit, qa, prod")

    logging.info(f"Entered input parameters. repo = {repoValue}, apiToken = {apiToken}, environment = {environment}, commitHash = {commitHash}")

    # Connecting to git hub


    g = Github(apiToken)

    repo = g.get_repo(repoValue)

    repos = repo.get_commit(sha="bf22201")
    print(f"repos.commit =  {repos}")
    commits = repo.get_commits(sha='prod')
    for element in commits:
        print(element)
    #print(f"commits =  {commits}")

    repos = g.get_repo(repoValue)
    pprint("repos = g.get_repo(ivshof/gitHabAPITest2")
    pprint(f"repos = {repos}")


    # Get the full list of repos for a user
    for repo in g.get_user().get_repos():
        print(repo.name)

    # Print content files
    # content = repo.get_contents("")
    # for content_file in content:
    #     print(content_file)

    repo = g.get_repo(repoValue)
    print("Branches:")
    branches = repo.get_branches()
    for branch in branches:
        print(branch)


    # Get the latest SHA for scpecidied environment (branch) in case it was not provided by the user
    if commitHash == 'none':
        latestCommit = g.get_repo(repoValue).get_branch(environment)
        latestCommitSHA = latestCommit.commit.sha
        commitHash = latestCommitSHA
        print(f"latestCommitSHA = {latestCommitSHA}")


    #Get the parent SHA
    repos = repo.get_commit(sha=commitHash)
    print(repos.commit.parents)

    diffCompare= repo.compare('bf222011ffc20947778cac86da6b03ec07388bcd', '321ced789d79886f4f58c880bec580377e51ec35')
    print(diffCompare.diff_url)
    print(diffCompare.files)







if __name__ == "__main__":
    main()


