# GIT HUB API Test tool
It is a simple git hub api test tool powered by PyGithub (https://github.com/PyGithub/PyGithub)

## How to use
```javascript
python git-test.py repo apiToken environment {commitHash}
```
## Parameters

- repo: repo name, like "ivshof/gitHabAPITestTool"
- apiToken: Personal access tokens (details: https://github.com/settings/tokens)
- environment: brunch name, like one from the list['dev', 'sit', 'qa', 'prod']
- commitHash: hash of the commit that will be used for diff changes


## Tool results
1) Identify changes ralated to provided commitHash or to the latest commit if commitHash was not provided
2) Filter changes based on configuration file extension (like '.yaml'
3) Validate the location of configuration files with hardcoded "validPaths" list
4) For each configuration file in list retrive content and print it in case configuration env is enabled. Env and configurations listd in "envConfiguration"
