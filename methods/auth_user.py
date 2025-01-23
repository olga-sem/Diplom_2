import requests
import allure
import helpers
import urls


class AuthUser:

    @allure.step('Метод для авторизации пользователя')
    def login_with_existing_data(self, payload):
        requests.post(f'{urls.BASE_URL}{urls.NEW_USER_URL}', data=payload)
        response = requests.post(f'{urls.BASE_URL}{urls.AUTH_URL}', data = payload)
        return [response.status_code, response.json()]

    @allure.step('Метод для авторизации пользователя с неправильной почтой')
    def login_with_wrong_email(self, email):
        user_data = helpers.create_new_user_and_return_auth_data()
        new_data = {
                   "email": email,
                   "password": user_data["password"]
                   }
        response = requests.post(f'{urls.BASE_URL}{urls.AUTH_URL}', data=new_data)
        return [response.status_code, response.json()]

    @allure.step('Метод для авторизации пользователя с неправильным паролем')
    def login_with_wrong_password(self, password):
        user_data = helpers.create_new_user_and_return_auth_data()
        new_data = {
            "email": user_data["email"],
            "password": password
        }
        response = requests.post(f'{urls.BASE_URL}{urls.AUTH_URL}', data=new_data)
        return [response.status_code, response.json()]
