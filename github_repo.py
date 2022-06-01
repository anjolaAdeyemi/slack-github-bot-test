import requests
from pprint import pprint
username = "anjola85"
url = f"https://api.github.com/users/defunkt"
user_data = requests.get(url).json();
pprint(user_data);
# https://api.github.com/repos/:owner/:repo/pulls?state=all
