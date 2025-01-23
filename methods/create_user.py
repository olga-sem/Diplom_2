import requests
import allure
import urls


class CreateUser:

    @allure.step('Метод для создания пользователя')
    def create_new_user(self, payload):
        response = requests.post(f'{urls.BASE_URL}{urls.NEW_USER_URL}', data = payload)
        return [response.status_code, response.json()]
