import requests
import urls
import allure


class UpdateUser:

    @allure.step('Метод для обновления почты авторизованного пользователя')
    def update_data_with_authorization(self, new_data, access_token):
        headers = {"Authorization": access_token}
        response = requests.patch(f'{urls.BASE_URL}{urls.UPDATE_URL}',
                                  json=new_data,
                                  headers=headers)
        return [response.status_code, response.json()]

    @allure.step('Метод для обновления почты неавторизованного пользователя')
    def update_data_without_authorization(self, new_data):
        headers = {"Authorization": ""}
        response = requests.patch(f'{urls.BASE_URL}{urls.UPDATE_URL}',
                                  json = new_data,
                                  headers=headers)
        return [response.status_code, response.json()]
