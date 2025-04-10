import requests

def get_user_info(base_url, username):
    return requests.get(f"{base_url}/users/{username}")
