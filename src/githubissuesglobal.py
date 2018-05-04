import os
import requests
import subprocess
import re

out = subprocess.Popen("git remote show origin".split(),
                       stdout=subprocess.PIPE).communicate()[0]
out = str(out.decode('utf8'))
prt = re.findall(r'https://.*', out)
repo = os.path.basename(prt[0])
repo = repo[:-4]
# extract repository name from this folder
request = requests.get("https://api.github.com/repos/dustinknopoff/{}/issues".format(repo),
                       headers={'Authorization': 'token '})  # insert valid token
# get all issues related to this repository
string = ""
for issue in request.json():
    # Generate formatted string for use
    string += "TODO: {}\n{}\n{}\n".format(
        issue['title'], issue['html_url'], issue['body'])
if string != "":
    # create txt file holding all templates
    with open(os.getcwd() + "/issues.txt", 'w+', encoding='utf8') as f:
        f.write(string)
else:
    print("This repository has no open issues.")
