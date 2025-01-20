import json
import os
import random
import requests
from jsonschema import validate

job = "leader"
name = "morpheus"


def test_status_code_create_user():
    response = requests.post('https://reqres.in/api/users/', data={"name": job, "job": name})

    assert response.status_code == 201, f"Unexpected status code {response.status_code}"


def test_chema_validate_create_users():
    response = requests.post('https://reqres.in/api/users/', data={"name": job, "job": name})

    # with open(os.path.join(os.path.dirname(__file__), 'json_schemas/post_schema.json')) as file:
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), f"./json_schemas/post_schema.json"))) as file:
        validate(response.json(), schema=json.loads(file.read()))


def test_response_create_user():
    response = requests.post('https://reqres.in/api/users/', data={"name": job, "job": name})
    body = response.json()

    assert body["name"] == job, f"Unexpected name  - {body["name"]}"
    assert body["job"] == name, f"Unexpected job - {body["job"]}"


def test_status_code_get_info_single_user():
    response = requests.get('https://reqres.in/api/users/2')

    assert response.status_code == 200, f"Unexpected status code {response.status_code}"


def test_status_code_get_info_single_user_not_found():
    random_number = random.randint(20, 50)
    response = requests.get('https://reqres.in/api/users/' + 'random_number')

    assert response.status_code == 404, f"Unexpected status code {response.status_code}"


def test_schema_validate_get_info_single_user():
    response = requests.get('https://reqres.in/api/users/2')

    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), f"./json_schemas/get_schema.json"))) as file:
        validate(response.json(), schema=json.loads(file.read()))


def test_status_code_update_user():
    response = requests.put('https://reqres.in/api/users/2', data={"job": "new_name"})

    assert response.status_code == 200, f"Unexpected status code {response.status_code}"


def test_response_update_user():
    response = requests.put('https://reqres.in/api/users/2', data={"job": "new_name"})
    body = response.json()

    assert body["job"] == "new_name", f"Unexpected job  - {body["job"]}"


def test_schema_validate_update_info_single_user():
    response = requests.put('https://reqres.in/api/users/2', data={"name": job, "job": name})

    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), f"./json_schemas/put_schema.json"))) as file:
        validate(response.json(), schema=json.loads(file.read()))


def test_status_code_delete_user():
    response = requests.delete('https://reqres.in/api/users/', data={"name": job, "job": name})

    assert response.status_code == 204, f"Unexpected status code {response.status_code}"


def test_successful_user_login():
    response = requests.post('https://reqres.in/api/login/',
                             data={"email": "eve.holt@reqres.in", "password": "cityslicka"})

    assert response.status_code == 200, f"Unexpected status code {response.status_code}"


def test_status_code_unsuccessful_user_login():
    response = requests.post('https://reqres.in/api/login/',  data={"email": "peter@klaven"})

    assert response.status_code == 400, f"Unexpected status code {response.status_code}"


def test_response_unsuccessful_login_missing_password():
    response = requests.post('https://reqres.in/api/login/',  data={"email": "peter@klaven"})
    body = response.json()

    assert body["error"] == "Missing password", f"Unexpected response  - {body["error"]}"

def test_response_unsuccessful_user_login_not_found():
    response = requests.post('https://reqres.in/api/login/',  data={"email": "eve.h446464olt@reqres.in", "password": "cityslicka"})
    body = response.json()

    assert body["error"] == "user not found", f"Unexpected response  - {body["error"]}"
