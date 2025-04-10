import json

import allure
import requests
from behave import given, when, then
from utilities.configurations import *
from utilities.resources import APIResources


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
    context.get_book_by_author_url = get_config()['API']['lirary_api_base_url'] + APIResources.get_book_by_author_resource
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
