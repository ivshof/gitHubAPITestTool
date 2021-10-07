# Test tool to check git hub commit changes

import sys
from github import Github
import os


def main():

    envPossibleValues = ['dev', 'sit', 'qa', 'prod']
    # string that will be used to filter changes for config (yaml) files
    filterConfigFileParameter = '.yaml'
    validPaths = [
        'config/rbac/corporate-services/admin.yaml',
        'config/rbac/corporate-services/readonly.yaml',
        'config/rbac/gaming/allusers.yaml',
        'config/rbac/gaming/systemusers.yaml',
        'config/topics/corporate-services/admin.yaml',
        'config/topics/corporate-services/readonly.yaml',
        'config/topics/gaming/allusers.yaml',
        'config/topics/gaming/systemusers.yaml']



    # Ensure correct usage of input parameters
    if len(sys.argv) < 4 or len(sys.argv) > 6:
        print("Input parameters ERROR")
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
        print("Input environment value ERROR")
        sys.exit("Usage: 'environment' possible values: dev, sit, qa, prod")

    print(f"Entered input parameters. repo = {repoValue}, apiToken = {apiToken}, environment = {environment}, commitHash = {commitHash}")

    # Connecting to git hub
    g = Github(apiToken)
    repo = g.get_repo(repoValue)

    # repos = g.get_repo(repoValue)
    # pprint("repos = g.get_repo(ivshof/gitHabAPITest2")
    # pprint(f"repos = {repos}")


    # Get the full list of repos for a user
    # for repo in g.get_user().get_repos():
    #     print(repo.name)

    # Print content files
    # content = repo.get_contents("")
    # for content_file in content:
    #     print(content_file)

    repo = g.get_repo(repoValue)
    # print("Branches:")
    # branches = repo.get_branches()
    # for branch in branches:
    #     print(branch)

    # Get the latest SHA for scpecidied environment (branch) in case it was not provided by the user
    if commitHash == 'none':
        latestCommit = g.get_repo(repoValue).get_branch(environment)

        latestCommitSHA = latestCommit.commit.sha
        commitHash = latestCommitSHA
        print(f"latestCommitSHA = {latestCommitSHA}")

    #repos = repo.get_commit(sha="ef159d2abe5474f981e5cf8ddf0f75c539054abb")
    #print(f"repos.commit =  {repos.files}")

    # Get commit hashes for all comits in branch (env)
    repo = g.get_repo(repoValue)
    # commits = repo.get_commits(sha=environment)
    # print(f"comits in {environment} branch:")
    # for element in commits:
    #     print(f"element = {element}")

        #
        # if len(element.files) > 0:
        #     print(type(element.files[0]))
        #     print(f"element = {element.files[0]}")
        #     print(f"element = {element.files}")

    # print(f"commits =  {commits}")

    # Get details about specified commit hash
    print(f"CommitSHA = {commitHash}")
    response = repo.get_commit(sha=commitHash).raw_data

    # print("raw data:")
    # print(response)

    parentCommitHash = response['parents'][0]['sha']
    print(f"parentCommitHash = {parentCommitHash}")

    # Check if configuration (yaml) files were modified
    configFileChanges = []
    for file in range(len(response['files'])):
        fileName = response['files'][file]['filename']
        if filterConfigFileParameter in fileName:
            shaForTheFileName = response['files'][file]['sha']
            configFileChanges.append({"filename": fileName, "sha": shaForTheFileName})

    if len(configFileChanges) == 0:
        print("No configuration (yaml) files were modified!")
        return



    # for file in raw_data['files']:
    #     print(f"FILE =  {raw_data['files'][file]['filename']}")

    # print(type(repos.commit.parents))
    # print(f'repos.commit.parents = {repos.commit.parents}')

    #print(repos.commit.parents['sha'])

    print(f"configFileChanges number= {len(configFileChanges)}")

    diffCompare = repo.compare(parentCommitHash, commitHash).raw_data
    #print(f"diffCompare = {diffCompare}")
    for file in range(len(diffCompare['files'])):
        fileName = diffCompare['files'][file]['filename']
        # print(f"fileName = {fileName}")

        if filterConfigFileParameter in fileName:
            if fileName in validPaths:
                print("File location is valid")
            else:
                print("File location is NOT valid")

            contents_url = diffCompare['files'][file]['contents_url']
            status = diffCompare['files'][file]['status']
            print(f">>>>> Diff Changes for FILE = {fileName},\n status = {status},\n contents_url={contents_url} \nFor Commits {parentCommitHash} -> {commitHash}")

            if 'patch' in diffCompare['files'][file]:
                comitDiffText = response['files'][file]['patch']
                print(f"CHANGES:\n====\n{comitDiffText}\n====\n")
            else:
                print("CHANGES:\n====\nNo changes in file content\n====\n")


            if validPaths


            print(f"contents_url = {contents_url}")
            print("<<<<<")




    # print(f"diff_url = {diffCompare.diff_url}")
    # print(f"diffCompare.total_commits = {diffCompare.total_commits}")
    # print(f"diffCompare.files = {diffCompare.files}")





    # for element in range(len(configFileChanges)):
    #     print(configFileChanges[element]['filename'])
    #     print(commitHash)
    #     #print(configFileChanges[element]['sha'])
    #
    #     comitToCompare = configFileChanges[element]['sha']
    #
    #     diffCompare= repo.compare(str(commitHash), str(comitToCompare))
    #     print(diffCompare.diff_url)
    #     print(type(diffCompare.files))



if __name__ == "__main__":
    main()


