# GIT HUB API Test tool
It is a simple git hub api test tool

## How to use
```javascript
python git-test.py repo apiToken environment {commitHash}
```
## Parameters

- repo: repo name, like "ivshof/gitHabAPITestTool"
- apiToken: Personal access tokens (details: https://github.com/settings/tokens)
- environment: brunch name, like one from the list['dev', 'sit', 'qa', 'prod']
- commitHash: hash of the commit that will be used for diff changes
