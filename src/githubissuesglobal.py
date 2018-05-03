import os
import requests

request = requests.get("https://api.github.com/repos/dustinknopoff/py-explore/issues",
                       headers={'Authorization': 'token '})  # enter token
string = ""
for issue in request.json():
    string += "TODO: {}\n{}\n{}\n".format(issue['title'], issue['html_url'], issue['body'])
if string != "":
    with open(os.getcwd() + "/issues.txt", 'w+', encoding='utf8') as f:
        f.write(string)
else:
    print("This repository has no open issues.")
