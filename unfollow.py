import requests

token = "YOUR-TOKEN" # genrate new token and paste here

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# List of special users to keep following
special_users = [
]

# Get the list of users you are following
response = requests.get("https://api.github.com/user/following", headers=headers)
following = response.json()

# Unfollow users who are not in the special_users list
for user in following:
    username = user["login"]
    if username not in special_users:
        unfollow_url = f"https://api.github.com/user/following/{username}"
        unfollow_response = requests.delete(unfollow_url, headers=headers)
        if unfollow_response.status_code == 204:
            print(f"Unfollowed {username}")
        else:
            print(f"Failed to unfollow {username}")
