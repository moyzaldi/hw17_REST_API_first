import json
import os
import requests
from jsonschema import validate
import allure

url = 'https://reqres.in/api/users'
job = "leader"
name = "morpheus"
payload = {"name": job, "job": name}
response = requests.post(url, data=payload)

@allure.tag('Registration')
def test_status_code_post():
    response = requests.post(url, data=payload)

    assert response.status_code == 201, f"Unexpected status code {response.status_code}"

@allure.tag('Registration')
def test_schema_validate():
    response = requests.post(url, data=payload)

    # with open(os.path.join(os.path.dirname(__file__), 'json_schemas/post_users.json')) as file:
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), f"./json_schemas/post_users.json"))) as file:
        validate(response.json(), schema=json.loads(file.read()))

@allure.tag('Registration')
def test_job_name_from_request_returns_in_body():
    response = requests.post(url, data=payload)
    body = response.json()

    assert body["name"] == job, f"Unexpected name  - {body["name"]}"
    assert body["job"] == name, f"Unexpected job - {body["job"]}"

@allure.tag('Registration')
def test_status_code_get():
    response = requests.get(url, params={"page": 1, "per_page": 6})


    assert response.status_code == 200, f"Unexpected status code {response.status_code}"