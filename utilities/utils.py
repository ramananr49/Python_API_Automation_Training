import json

import requests

def get_user_info(base_url, username):
    return requests.get(f"{base_url}/users/{username}")


def create_book_payload(name, isbn, aisle, author):
    payload = {}
    payload['name'] = name
    payload['isbn'] = isbn
    payload['aisle'] = aisle
    payload['author'] = author
    return payload