import os
import sys

from github import Github

g = Github("")  # enter your github token
# Get repository
repo = g.get_user().get_repo(sys.argv[1])
issues = []
counter = 1
# Show all issues
for issue in repo.get_issues():
    print(str(counter) + ". " + issue.title)
    issues.append(issue)
    counter += 1
string = ""
# Create template for each issue as a todo
for issue in issues:
    string += "TODO: {}\n{}\n{}\n".format(issue.title,
                                          issue.html_url, issue.body)
if string != "":
    # write to current directory
    with open(os.getcwd() + "/issues.txt", 'w+', encoding='utf8') as f:
        f.write(string)
else:
    print("This repository has no open issues.")
