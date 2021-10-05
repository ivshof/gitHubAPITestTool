import requests
import os
from pprint import pprint

token = "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"
owner = "ivshof"
repo = "gitHabAPITest2"
query_url = f"https://api.github.com/repos/{owner}/{repo}/"
params = {
    "state": "open",
}
headers = {'Authorization': f'token {token}'}
r = requests.get(query_url, headers=headers, params=params)
pprint(r.json())