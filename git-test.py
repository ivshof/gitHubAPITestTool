# Test tool to check git hub commit changes

import sys
from github import Github
import os
import base64

def main():

    envPossibleValues = ['dev', 'sit', 'qa', 'prod']

    # string that will be used to filter changes for config (yaml) files
    filterConfigFileParameter = '.yaml'

    # valid paths to configuration files
    validPaths = ['config/rbac/corporate-services/admin.yaml',
                  'config/rbac/corporate-services/readonly.yaml',
                  'config/rbac/gaming/allusers.yaml',
                  'config/rbac/gaming/systemusers.yaml',
                  'config/topics/corporate-services/admin.yaml',
                  'config/topics/corporate-services/readonly.yaml',
                  'config/topics/gaming/allusers.yaml',
                  'config/topics/gaming/systemusers.yaml']

    envConfiguration = {'rbac': {'dev': 'false', 'sit': 'true', 'qa': 'false', 'prod':'false'},
                        'topics': {'dev': 'true', 'sit': 'true', 'qa': 'false', 'prod': 'false'}}


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

    print(f"Entered input parameters. repo = {repoValue}, apiToken = *****, environment = {environment}, commitHash = {commitHash}")

    # Connecting to git hub
    g = Github(apiToken)
    repo = g.get_repo(repoValue)

    # Get the latest SHA for scpecidied environment (branch) in case it was not provided by the user
    if commitHash == 'none':
        latestCommit = g.get_repo(repoValue).get_branch(environment)
        latestCommitSHA = latestCommit.commit.sha
        commitHash = latestCommitSHA
        print(f"latestCommitSHA = {latestCommitSHA}")

    # Get details for specified commit SHA
    response = repo.get_commit(sha=commitHash).raw_data
    parentCommitHash = response['parents'][0]['sha']

    # Check if configuration (yaml) files were modified
    configFileChanged = []


    for file in range(len(response['files'])):
        fileName = response['files'][file]['filename']
        if filterConfigFileParameter in fileName:
            shaForTheFileName = response['files'][file]['sha']
            configFileChanged.append({"filename": fileName, "sha": shaForTheFileName})


    if len(configFileChanged) == 0:
        print("No configuration (yaml) files were modified!")
        return
    else:
        print(f"\nFollowing configuration files have changed, Number = {len(configFileChanged)}: ")
        for filenames in configFileChanged:
            print(filenames)


    # Compare provided (or latest commit) with the previous one
    diffCompare = repo.compare(parentCommitHash, commitHash).raw_data

    print("\nFILES DIFF RESULT")
    for file in range(len(diffCompare['files'])):
        validCheck = 'false'
        fileName = diffCompare['files'][file]['filename']

        #  Check if configuration (yaml) files were modified
        if filterConfigFileParameter in fileName:

            status = diffCompare['files'][file]['status']
            print(f">>>>>\nDiff Changes for FILE = {fileName},\nstatus = {status},\nFor Commits {parentCommitHash} -> {commitHash}")

            # Check if file is stored in valud path define in validPaths list
            if fileName in validPaths:
                print("File location is valid")
                validCheck = 'true'
            else:
                print("File location is NOT valid")

            # List diff in file content
            if 'patch' in diffCompare['files'][file]:
                comitDiffText = response['files'][file]['patch']
                print(f"CHANGES:\n====\n{comitDiffText}\n====\n")
            else:
                print("CHANGES:\n====\nNo changes in file content\n====\n")

            # For validated files get the file content, and print it in case environment is enabled
            if validCheck == 'true':
                print('location validCheck Passed')
                pathList = fileName.split("/")
                obtainedEnvCfg = pathList[1]

                # Check if Env is enabled, and print the file content
                if obtainedEnvCfg in envConfiguration:
                    if envConfiguration[obtainedEnvCfg][environment] == 'true':
                        print(f"Environment check PASSED. {environment} = {envConfiguration[obtainedEnvCfg][environment]}")
                        print(f"fileName= {fileName} Content:")
                        contents = repo.get_contents(fileName, ref=environment).content

                        #decode from base64 to string
                        contents = base64ToString(contents)
                        print(contents)

                    else:
                        print(f"Environment check NOT PASSED . {environment} = {envConfiguration[obtainedEnvCfg][environment]}")

            print("<<<<<\n")


def base64ToString(text):
    return base64.b64decode(text).decode('utf-8')

if __name__ == "__main__":
    main()


