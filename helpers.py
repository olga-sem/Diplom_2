import string
import random


def create_new_user_and_return_auth_data():
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    email = generate_random_string() + '@gmail.com'
    password = generate_random_string()
    name = generate_random_string()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload


def create_data_for_update():
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    email = generate_random_string() + '@gmail.com'
    name = generate_random_string()
    new_data = {
        "email": email,
        "name": name
    }
    return new_data