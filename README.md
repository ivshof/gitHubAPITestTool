# GIT HUB API Test tool
It is a simple git hub api test tool powered by PyGithub (https://github.com/PyGithub/PyGithub)

## How to use
```javascript
python git-test.py repo apiToken environment {commitHash}
```
## Parameters

- repo: repo name, like "ivshof/gitHubAPITestTool"
- apiToken: Personal access tokens (details: https://github.com/settings/tokens)
- environment: brunch name, like one from the list['dev', 'sit', 'qa', 'prod']
- commitHash: hash of the commit that will be used for diff changes


## Results

1. Identify changes related to provided commit hash or to the latest commit if the commit hash was not provided

2. Filter changes based on the configuration file extension (like '.yaml'

3. Validate the location of configuration files with a hardcoded "validates" list

4. For each configuration file in the list retrieve content and print it in case configuration env is enabled. Env and configurations listed in "envConfiguration"
