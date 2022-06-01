import slack
import os
import requests
from pprint import pprint
from pathlib import Path
from dotenv import load_dotenv

# loading environment variable
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])


repo = "slack-github-bot-test"
username = "anjolaAdeyemi"
url = "https://api.github.com/repos/" + username + "/" + repo + "/git/commits/b2ce0ca431b6166e841fa3a447e4e5620e7a4f4b"
user_data = requests.get(url).json();


# users github profile link should be embedded
user = user_data['committer']['name']

# pr number and name should be displayed with embeded link to the PR
pr_name = "name of pr"

# commit message + description
commit_message = user_data['message']
description = "description of commit"

# link to reviewers should be displayed
reviewers = "commerce team"


message = "\nPull request opened by=> " + user + "\nPull request name=> " + pr_name + "\ncommit message and commit number=> " + commit_message + "\nDescription=> " + description + "\nreviewers=> " + reviewers

# pprint(user_data['committer']);
# dict_keys(['sha', 'node_id', 'url', 'html_url', 'author', 'committer', 'tree', 'message', 'parents', 'verification'])
# repo_name, name_of_person that opened the pr, name_of_the_pr, commit_message_and_description, reviewers_names

pprint(user_data)

# client.chat_postMessage(channel='#test', text=message)
