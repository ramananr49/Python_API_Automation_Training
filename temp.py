import json

import requests
from utilities.configurations import *
from utilities.resources import APIResources


#Get Book by Author
get_api_url = get_config()['API']['lirary_api_base_url'] + APIResources.get_book_by_author_resource
param = { "AuthorName" : "Lewis Hamilton" }
response = requests.get(get_api_url, params=param)
print(response.status_code)
print(response.json())
print(json.dumps(response.json(), indent=2))


# #Get Book by ID
# get_book_by_id_url = get_config()['API']['lirary_api_base_url'] + APIResources.get_book_by_ID_resource
# param = {'ID' : "RRAY0021"}
# book_by_id_response = requests.get(get_book_by_id_url, params=param)
# print(book_by_id_response.status_code)
# print(book_by_id_response.json())
# print(json.dumps(book_by_id_response.json(), indent=2))
#
# #Post Book
# add_book_url = get_config()['API']['lirary_api_base_url'] + APIResources.add_book_resource
# payload = {
#     "name" : "temp",
#     "isbn" : "RR",
#     "aisle" : "44",
#     "author" : "temp"
# }
# add_book_response = requests.post(add_book_url, json=payload)
# print(add_book_response.status_code)
# print(add_book_response.json())
# book_ID = add_book_response.json()["ID"]
# print(book_ID)
#
# #Delete Book
delete_book_url = get_config()['API']['lirary_api_base_url'] + APIResources.delete_book_resource
delete_payload = {
    "ID" : "RRAY0011"
}
delete_book_response = requests.post(delete_book_url, json=delete_payload)
print(delete_book_response.status_code)
print(delete_book_response.json())