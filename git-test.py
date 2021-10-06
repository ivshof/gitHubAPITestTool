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

    repos = repo.get_commit(sha="ef159d2abe5474f981e5cf8ddf0f75c539054abb")
    print(f"repos.commit =  {repos.files}")
    # print(f"element repos.files[0] = {repos.files[0]}")
    # print(f"element repos.files[0] = {repos.files[0]}")
    # if "log.txt" in repos.files:
    #     print("paass")

    # Get commit hashes for all comits in branch (env)
    repo = g.get_repo(repoValue)
    commits = repo.get_commits(sha=environment)
    print(f"comits in {environment} branch:")
    for element in commits:
        print(f"element = {element}")


        #
        # if len(element.files) > 0:
        #     print(type(element.files[0]))
        #     print(f"element = {element.files[0]}")
        #     print(f"element = {element.files}")



    # print(f"commits =  {commits}")

    #Get the parent SHA
    print(f"ComitSHA = {commitHash}")
    repos = repo.get_commit(sha=commitHash)
    raw_data = repos.raw_data
    print("raw data:")
    print(raw_data)
    #print(raw_data['files'])
    #print(type(raw_data['files'][0]))
    print(f"filename = {raw_data['files'][0]['filename']}")
    print(f"sha = {raw_data['files'][0]['sha']}")
    print(f"parentSHA = {raw_data['parents'][0]['sha']}")
    #print(f"raw_data = {raw_data}")

    print(type(repos.commit.parents))
    print(f'repos.commit.parents = {repos.commit.parents}')

    #print(repos.commit.parents['sha'])
    for i in repos.commit.parents:
        print(type(i))
        print(i)





    diffCompare= repo.compare('aa342a24b55bd5824d661663a774c7cf4a2ffa6f', '3371ae298fbcf5c4dbfdf865137a8366e6a834f9')
    print(diffCompare.diff_url)

    print(type(diffCompare.files))
    for i in diffCompare.files:
        print(i)
        print(type(i))






if __name__ == "__main__":
    main()


