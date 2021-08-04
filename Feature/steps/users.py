from behave import when, then
from hamcrest import assert_that, equal_to, has_key
import requests
import datetime

url = "https://reqres.in/api/users"
urlWithParams = url
user = dict()
resp = dict()
userId = int()
pageNumber = int()


@when('the user name "{name}" is defined in the name parameter')
def step_impl(context, name):
    global user
    user["name"] = name


@when('the user job "{job}" is defined in the job parameter')
def step_impl(context, job):
    global user
    user["job"] = job


@when('the {method} request is sent')
def step_impl(context, method):
    global url
    global user
    global resp
    context.response = requests.request(method.capitalize(), url, data=user)
    if method != "delete":
        resp = dict(context.response.json())


@then('the response code has been {code}')
def step_impl(context, code: int):
    assert_that(context.response.status_code, equal_to(int(code)))


@then('the response contains the submitted name "{name}"')
def step_impl(context, name):
    global resp
    has_key("name")
    assert_that(resp["name"], equal_to(name))


@then('the response contains the submitted job "{job_text}"')
def step_impl(context, job_text):
    global resp
    has_key("job")
    assert_that(resp["job"], equal_to(job_text))


@then("the response must contain the id field")
def step_impl(context):
    has_key("id")


@then("the response contains a createAt field")
def step_impl(context):
    global resp
    assert_that((str(resp["createdAt"]).split('T')[0]), equal_to(str(datetime.datetime.now()).split(" ")[0]))


@when("the request to list all users is sent")
def step_impl(context):
    global urlWithParams
    global user
    global resp
    context.response = requests.request("GET", urlWithParams)
    resp = dict(context.response.json())


@when("the page {page_text} number is established in the parameter of the request")
def step_impl(context, page_text):
    global urlWithParams
    global pageNumber
    pageNumber = page_text
    urlWithParams = f"{url}?page={pageNumber}"


@then("the response contains the submitted page {page_text}")
def step_impl(context, page_text):
    global resp
    has_key("page")
    assert_that((resp["page"]), equal_to(int(page_text)))


@then("the response contains the user number per pages {user_per_page}")
def step_impl(context, user_per_page):
    global resp
    has_key("per_page")
    assert_that((resp["per_page"]), equal_to(int(user_per_page)))


@then("the response contains the total users {total_user_text}")
def step_impl(context, total_user_text):
    global resp
    has_key(equal_to("total"))
    assert_that((resp["total"]), equal_to(int(total_user_text)))


@then("the response contains the total page {total_pages}")
def step_impl(context, total_pages):
    global resp
    has_key(equal_to("total_pages"))
    assert_that((resp["total_pages"]), equal_to(int(total_pages)))


@then("the response contains a data parameter with the total user {total_users}")
def step_impl(context, total_users):
    global resp
    has_key(equal_to("data"))
    assert_that((len(resp["data"])), equal_to(int(total_users)))


@then("the response contains a support parameter")
def step_impl(context):
    has_key("avatar")


@then("the support parameter contains the url {url_text} field")
def step_impl(context, url_text):
    global resp
    has_key("url")
    assert_that((resp["support"]["url"]), equal_to(url_text))


@then("the support parameter contains the text {text_text} field")
def step_impl(context, text_text):
    global resp
    has_key("text")
    assert_that((resp["support"]["text"]), equal_to(text_text))


@when('the user id {id_text} is defined as a parameter')
def step_impl(context, id_text):
    global url
    global userId
    userId = id_text
    url = f"{url}/{userId}"


@then("the data parameter contains the email {email_text} parameter")
def step_impl(context, email_text):
    global resp
    has_key("email")
    assert_that((resp["data"]["email"]), equal_to(email_text))


@then("the data parameter contains the first_name {first_name_text} parameter")
def step_impl(context, first_name_text):
    global resp
    has_key("first_name")
    assert_that((resp["data"]["first_name"]), equal_to(first_name_text))


@then("the data parameter contains the last_name {last_name_text} parameter")
def step_impl(context, last_name_text):
    global resp
    has_key("last_name")
    assert_that((resp["data"]["last_name"]), equal_to(last_name_text))


@then("the data parameter contains the avatar {avatar_url} parameter")
def step_impl(context, avatar_url):
    global resp
    has_key("avatar")
    assert_that((resp["data"]["avatar"]), equal_to(avatar_url))


@then("the response contains a updateAt field")
def step_impl(context):
    global resp
    assert_that((str(resp["updatedAt"]).split('T')[0]), equal_to(str(datetime.datetime.now()).split(" ")[0]))


@then('the response must contain the id {id_text} sent')
def step_impl(context, id_text: int):
    global resp
    has_key("id")
    assert_that((resp["data"]["id"]), equal_to(int(id_text)))
