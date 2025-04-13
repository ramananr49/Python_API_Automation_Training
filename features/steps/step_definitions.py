import json
import allure
import requests
import sys
import os
from behave import given, when, then
from utilities.configurations import *
from utilities.resources import APIResources
from utilities.utils import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@given("the GitHub API is available")
def step_impl(context):
    context.base_url = "https://api.github.com"
    allure.attach(context.base_url, name="API Endpoint", attachment_type=allure.attachment_type.TEXT)


@when('I request the user info for "{username}"')
def step_impl(context, username):
    context.response = requests.get(f"{context.base_url}/users/{username}")
    allure.attach(str(context.response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)
    allure.attach(context.response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)


@then("the response status code should be 200")
def step_impl(context):
    assert context.response.status_code == 200
    allure.attach("Assertion Passed: Status code is 200", name="Assertion Result",
                  attachment_type=allure.attachment_type.TEXT)


@given('the Get book by Author API is available')
def step_impl(context):
    context.get_book_by_author_url = get_config()['API'][
                                         'lirary_api_base_url'] + APIResources.get_book_by_author_resource
    context.param = {"AuthorName": "Lewis Hamilton"}
    allure.attach(context.get_book_by_author_url, name="API Endpoint", attachment_type=allure.attachment_type.TEXT)


@when('I request the user info for Lewis Hamilton')
def step_impl(context):
    context.get_book_by_author_response = requests.get(context.get_book_by_author_url, params=context.param)
    allure.attach(str(context.get_book_by_author_response.status_code), name="Status Code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.get_book_by_author_response.json(), indent=2), name="Response body",
                  attachment_type=allure.attachment_type.JSON)


@then('the response status code should be 200 and book details fetched')
def step_impl(context):
    assert context.get_book_by_author_response.status_code == 200
    allure.attach("Assertion Passed and Status Code is 200", name="Assertion Result",
                  attachment_type=allure.attachment_type.TEXT)


@given('the Get Book By ID API is Available')
def step_impl(context):
    context.get_book_by_id_url = get_config()['API']['lirary_api_base_url'] + APIResources.get_book_by_ID_resource
    allure.attach(context.get_book_by_id_url, name="Get Book By ID API Endpoint",
                  attachment_type=allure.attachment_type.TEXT)


@when('I request the book {IDs}')
def step_impl(context, IDs):
    context.param = {"ID": IDs}
    context.get_book_by_id_response = requests.get(context.get_book_by_id_url, params=context.param)
    allure.attach(str(context.get_book_by_id_response.status_code), name="Status Code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.get_book_by_id_response.json(), indent=2), name="Response Body",
                  attachment_type=allure.attachment_type.JSON)


@then('the response status code is 200 and desire book details fetched')
def step_impl(context):
    assert context.get_book_by_id_response.status_code == 200
    allure.attach("Assertion successful and Status code is 200", name="Assertion Result",
                  attachment_type=allure.attachment_type.TEXT)


@given('the Add Book API is available')
def step_impl(context):
    context.add_book_api_url = get_config()['API']['lirary_api_base_url'] + APIResources.add_book_resource
    context.add_book_payload = create_book_payload("Learn Cypress", "RRAY", "0011", "Lewis Hamilton")
    allure.attach(str(context.add_book_api_url), name="Add Book API Enfpoint",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.add_book_payload, indent=2), name="Request Body or Payload",
                  attachment_type=allure.attachment_type.JSON)


@when('execute the post request to add the book')
def step_impl(context):
    context.add_book_response = requests.post(context.add_book_api_url, json=context.add_book_payload)
    allure.attach(str(context.add_book_response.status_code), name="Status Code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.add_book_response.json()), name="Response Body",
                  attachment_type=allure.attachment_type.JSON)
    allure.attach(str(context.add_book_response.json()['ID']), name="ID of the book",
                  attachment_type=allure.attachment_type.TEXT)
    context.book_ID = context.add_book_response.json()['ID']


@then('the book should added successfully and status code is 200')
def step_impl(context):
    assert context.add_book_response.status_code == 200
    assert context.add_book_response.json()['Msg'] == "successfully added"
    allure.attach(f"Assertion successful, Book is created and ID of the book is {context.book_ID}",
                  name="Assertion Result", attachment_type=allure.attachment_type.TEXT)


@given(u'the Delete Book API is available')
def step_impl(context):
    context.delete_book_api_url = get_config()['API']['lirary_api_base_url'] + APIResources.delete_book_resource
    context.delete_payload = {"ID": context.book_ID}
    allure.attach(context.delete_book_api_url, name="Delete Book API Endpoint",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.delete_payload, indent=2), name="Request Body or Delete book API Payload",
                  attachment_type=allure.attachment_type.JSON)


@when(u'execute the post request to delete the book')
def step_impl(context):
    context.delete_book_response = requests.post(context.delete_book_api_url, json=context.delete_payload)
    allure.attach(str(context.delete_book_response.status_code), name="Status Code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.delete_book_response.json()), name="Response Body",
                  attachment_type=allure.attachment_type.JSON)


@then(u'the book should deleted successfully and status code is 200')
def step_impl(context):
    assert context.delete_book_response.status_code == 200
    assert context.delete_book_response.json()['msg'] == "book is successfully deleted"
    allure.attach("Assertion successful, Book is deleted and message is " + context.delete_book_response.json()['msg'],
                  name="Assertion Result",
                  attachment_type=allure.attachment_type.TEXT)


##Pet STore API
@given('the create user api details are available')
def step_impl(context):
    context.create_user_url = get_config()['API']['pet_store_api_base_url'] + APIResources.create_user_resource
    context.create_user_payload = create_user_payload(1129, "LH44", "Lewis", "Hamilton", "lewishamilton@gmail.com",
                                                      "Hammer44", "8144551058", 1)
    allure.attach(str(context.create_user_url), name="Create User API EndPoint",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.create_user_payload, indent=2), name="Create User Payload",
                  attachment_type=allure.attachment_type.JSON)


@when('I execute the create user api with valid data')
def step_impl(context):
    context.create_user_response = requests.post(context.create_user_url, json=context.create_user_payload)
    allure.attach(str(context.create_user_response.status_code), name="Status Code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.create_user_response.json(), indent=2), name="Response Body",
                  attachment_type=allure.attachment_type.JSON)


@then('The API call should be successful and user is created')
def step_impl(context):
    assert context.create_user_response.status_code == 200
    allure.attach("Assertion Successful! User is created and status code is 200", name="Assertion Result",
                  attachment_type=allure.attachment_type.TEXT)


@given('the get user by username api details are available')
def step_impl(context):
    context.user_ID = "LH44"
    context.get_user_by_username_url = get_config()['API'][
                                           'pet_store_api_base_url'] + APIResources.get_user_by_username_resource + context.user_ID
    allure.attach(str(context.get_user_by_username_url), name="Get User API EndPoint",
                  attachment_type=allure.attachment_type.TEXT)


@when('I execute the get user api with valid data')
def step_impl(context):
    context.get_user_response = requests.get(context.get_user_by_username_url)
    allure.attach(str(context.get_user_response.status_code), name="Status Code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.get_user_response.json(), indent=2), name="Response Body",
                  attachment_type=allure.attachment_type.JSON)


@then('The API call should be successful and user is fetched')
def step_impl(context):
    assert context.get_user_response.status_code == 200
    assert context.get_user_response.json()['id'] == 1129
    assert context.get_user_response.json()['username'] == "LH44"
    assert context.get_user_response.json()['firstName'] == "Lewis"
    assert context.get_user_response.json()['lastName'] == "Hamilton"
    assert context.get_user_response.json()['email'] == "lewishamilton@gmail.com"
    assert context.get_user_response.json()['password'] == "Hammer44"
    assert context.get_user_response.json()['phone'] == "8144551058"
    assert context.get_user_response.json()['userStatus'] == 1
    allure.attach("Assertion Successful! User is fetched and status code is 200", name="Assertion Result",
                  attachment_type=allure.attachment_type.TEXT)


@given('the Update api details are available')
def step_impl(context):
    context.user_ID = "LH44"
    context.update_user_url = get_config()['API'][
                                  'pet_store_api_base_url'] + APIResources.update_user_resource + context.user_ID
    context.payload = create_user_payload(1129, "LH44", "LEWIS", "HAMILTON", "LEWISHAMILTON@GMAIL.COM", "HAMMER44",
                                          "8144551058", 1)
    allure.attach(str(context.update_user_url), name="Update User API EndPoint",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.payload, indent=2), name="Update User Payload",
                  attachment_type=allure.attachment_type.JSON)


@when(u'I execute the update user api with valid data')
def step_impl(context):
    context.update_user_response = requests.put(context.update_user_url, json=context.payload)
    allure.attach(str(context.update_user_response.status_code), name="Status Code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.update_user_response.json(), indent=2), name="Response boody",
                  attachment_type=allure.attachment_type.JSON)


@then(u'The API call should be successful and user is updated')
def step_impl(context):
    assert context.update_user_response.status_code == 200
    assert context.update_user_response.json()['code'] == 200
    assert context.update_user_response.json()['message'] == "1129"
    allure.attach("Assertion Successful! User is updated and status code is 200", name="Assertion Result",
                  attachment_type=allure.attachment_type.TEXT)


@given(u'the delete api details are available')
def step_impl(context):
    context.user_ID = "LH44"
    context.delete_user_url = get_config()['API'][
                                  'pet_store_api_base_url'] + APIResources.delete_user_resource + context.user_ID
    allure.attach(context.delete_user_url, name="Delete User API EndPoint", attachment_type=allure.attachment_type.TEXT)


@when(u'I execute the delete user api with valid data')
def step_impl(context):
    context.delete_user_response = requests.delete(context.delete_user_url)
    allure.attach(str(context.delete_user_response.status_code), name="Status Code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(json.dumps(context.delete_user_response.json(), indent=2), name="Response body",
                  attachment_type=allure.attachment_type.JSON)


@then(u'The API call should be successful and user is deleted')
def step_impl(context):
    assert context.delete_user_response.status_code == 200
    assert context.delete_user_response.json()["code"] == 200
    assert context.delete_user_response.json()["message"] == "LH44"
    allure.attach("Assertion Successful! User is DELETED and status code is 200", name="Assertion Result",
                  attachment_type=allure.attachment_type.TEXT)
