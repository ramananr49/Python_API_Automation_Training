import requests
from utilities.configurations import *
from utilities.resources import APIResources

get_api_url = get_config()['API']['lirary_api_base_url'] + APIResources.get_book_by_author_resource

param = { "AuthorName" : "Lewis Hamilton" }
response = requests.get(get_api_url, params=param)
print(response.status_code)
print(response.json())