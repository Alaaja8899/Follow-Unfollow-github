import requests
import time

USERNAME = 'Your-username'
TOKEN = 'Your-Token' # get github token
TARGET_USER = '' #who you get his followers

def follow_followers(username, token, target_user):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    session = requests.Session()
    session.headers.update(headers)
    
    followers_url = f'https://api.github.com/users/{target_user}/followers'
    follow_url_template = 'https://api.github.com/user/following/{username}'
    
    page = 1
    
    while True:
        response = session.get(followers_url, params={'per_page': 100, 'page': page})
        response.raise_for_status()
        followers = response.json()
        
        if not followers:
            break
        
        for follower in followers:
            follower_username = follower['login']
            follow_url = follow_url_template.format(username=follower_username)
            response = session.put(follow_url)
            
            if response.status_code == 204:
                print(f'Successfully followed {follower_username}')
            elif response.status_code == 429:
                print('Rate limit exceeded. Waiting for 60 seconds before retrying...')
                time.sleep(60)
                response = session.put(follow_url)
                if response.status_code == 204:
                    print(f'Successfully followed {follower_username} after retrying')
                else:
                    print(f'Failed to follow {follower_username} after retrying: {response.status_code}')
            else:
                print(f'Failed to follow {follower_username}: {response.status_code}')
        
        page += 1

follow_followers(USERNAME, TOKEN, TARGET_USER)
