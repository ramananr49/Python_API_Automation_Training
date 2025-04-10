import allure
import requests
from behave import given, when, then


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
    allure.attach("Assertion Passed: Status code is 200", name="Assertion Result", attachment_type=allure.attachment_type.TEXT)