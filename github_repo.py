import requests
from pprint import pprint
repo = "slack-github-bot-test"
username = "anjolaAdeyemi"
url = "https://api.github.com/repos/" + username + "/" + repo + "/git/commits/b2ce0ca431b6166e841fa3a447e4e5620e7a4f4b"
user_data = requests.get(url).json();
pprint(user_data);




# https://api.github.com/repos/:owner/:repo/pulls?state=all
# curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/anjolaAdeyemi/slack-github-bot-test/git/commits/b2ce0ca431b6166e841fa3a447e4e5620e7a4f4b
# comments for developppp
# comments for develop