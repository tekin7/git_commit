import requests
import base64

github_username = ""
github_repo_name = ""
csv_file = "" 
github_token == ""
url = f'https://api.github.com/repos/{github_username}/{github_repo_name}/contents/{csv_file}?access_token=' +github_token
r = requests.get(url)
sha = r.json()['sha'] # target repo sha 

with open(csv_file, 'rb') as f:
    content = str(base64.b64encode(f.read()), encoding='utf8')
    data = {'message': 'bla bla', 'content': content, 'sha': sha, 'branch': 'master'}
    r_to_github = requests.put(url, json=data)