import json

import requests
from utilities.configurations import *
from utilities.resources import APIResources

# Add Pet to the store
# add_pet_url = "https://petstore.swagger.io/v2"
# add_pet_resource = '/pet'
# post_add_pet_url = add_pet_url + add_pet_resource
# payload = {
#
#   "id": 1129,
#   "category": {
#     "id": 33,
#     "name": "Dogs"
#   },
#   "name": "Tommy",
#   "photoUrls": [
#     ""
#   ],
#   "tags": [
#     {
#       "id": 33,
#       "name": "Dogs"
#     }
#   ],
#   "status": "available"
# }

# response = requests.post(post_add_pet_url, json=payload)
# print(response.status_code)
# print(json.dumps(response.json(), indent=2))


#Get Pet by ID
# pet_ID = 1129
# API_Endpoint = f"https://petstore.swagger.io/v2/pet/{pet_ID}"
# response = requests.get(API_Endpoint)
# print(response.status_code)
# print(json.dumps(response.json(), indent=2))

#updates a pet in the store with form data
# API_Endpoint = f"https://petstore.swagger.io/v2/pet/{pet_ID}"
# param = {
#     "name": "TOMMY",
#     "status" : "sold"
# }
# response = requests.post(API_Endpoint, params=param)
# print(response.status_code)
# print(json.dumps(response.json(), indent=2))


# #Create User
# create_user_api_url = "https://petstore.swagger.io/v2/user"
# payload = {
#   "id": 1129,
#   "username": "LH44",
#   "firstName": "Lewis",
#   "lastName": "Hamilton",
#   "email": "lewishamilton@gmail.com",
#   "password": "Hammer44",
#   "phone": "8144551058",
#   "userStatus": 1
# }
# response = requests.post(create_user_api_url, json=payload)
# print(response.status_code)
# print(json.dumps(response.json(), indent=2))

#Get user by username
username = "LH44"
get_user_by_username_url = f"https://petstore.swagger.io/v2/user/{username}"
response = requests.get(get_user_by_username_url)
print(response.status_code)
print(json.dumps(response.json(), indent=2))


#Update User
# username = "LH44"
# update_user_url = f"https://petstore.swagger.io/v2/user/{username}"
# payload = {
#   "id": 1129,
#   "username": "LH44",
#   "firstName": "LEWIS",
#   "lastName": "HAMILTON",
#   "email": "LEWISHAMILTON@GMAIL.COM",
#   "password": "HAMMER44",
#   "phone": "8144551058",
#   "userStatus": 1
# }
# response = requests.put(update_user_url, json=payload)
# print(response.status_code)
# print(json.dumps(response.json(), indent=2))


#Delete USer
# username = "LH44"
# delete_user_url = f"https://petstore.swagger.io/v2/user/{username}"
# response = requests.delete(delete_user_url)
# print(response.status_code)
# print(json.dumps(response.json(), indent=2))