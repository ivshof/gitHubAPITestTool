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

    repo = str(sys.argv[1])
    apiToken = str(sys.argv[2])
    environment = str(sys.argv[3])











    # Check if environment is in list of possible values
    if environment not in envPossibleValues:
        logging.info("Input environment value ERROR")
        sys.exit("Usage: 'environment' possible values: dev, sit, qa, prod")

    logging.info(f"Entered input parameters. repo = {repo}, apiToken = {apiToken}, environment = {environment}, commitHash = {commitHash}")

    # Connecting to git hub


    g = Github(apiToken)

    repo = g.get_repo("ivshof/gitHabAPITest2")
    issues = repo.get_issues(state="open")
    pprint(issues.get_page(0))

    repos = repo.get_commit(sha="bf22201")
    pprint(repos)

    repos = g.get_repo("ivshof/gitHabAPITest2")
    pprint("repos = g.get_repo(ivshof/gitHabAPITest2")
    pprint(repos)
    pprint("")

    # Get the full list of repos for a user
    for repo in g.get_user().get_repos():
        print(repo.name)

    # Print content files
    content = repo.get_contents("")
    for content_file in content:
        print(content_file)

    # Print content files
    content = repo.get_contents(ref='commit')
    for content_file in content:
        print(content_file)



if __name__ == "__main__":
    main()