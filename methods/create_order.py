import requests
import urls
import allure


class CreateOrder:

    @allure.step('Метод для создания заказа авторизованным пользователем с указанием ингредиентов')
    def create_order_with_authorization_and_ingredients(self, access_token):
        headers = {"Authorization": access_token}
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa70"]}
        response = requests.post(f'{urls.BASE_URL}{urls.ORDER_URL}',
                                 headers=headers,
                                 json=ingredients)
        return [response.status_code, response.json()]

    @allure.step('Метод для создания заказа авторизованным пользователем без указания ингредиентов')
    def create_order_without_ingredients(self, access_token):
        headers = {"Authorization": access_token}
        ingredients = {"ingredients": []}
        response = requests.post(f'{urls.BASE_URL}{urls.ORDER_URL}',
                                 headers=headers,
                                 json=ingredients)
        return [response.status_code, response.json()]

    @allure.step('Метод для создания заказа авторизованным пользователем с неправильным хешем ингредиентов')
    def create_order_with_wrong_hash(self, access_token):
        headers = {"Authorization": access_token}
        ingredients = {"ingredients": ["61c0c5trytyuiid"]}
        response = requests.post(f'{urls.BASE_URL}{urls.ORDER_URL}', headers=headers, json=ingredients)
        if response.status_code == 500:
            try:
                response_json = response.json()
            except ValueError:
                response_json = response.text
        else:
            response_json = {}

        return [response.status_code, response_json]

    @allure.step('Метод для создания заказа неавторизованным пользователем')
    def create_order_without_authorization(self):
        headers = {"Authorization": ""}
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa70"]}
        response = requests.post(f'{urls.BASE_URL}{urls.ORDER_URL}',
                                 headers=headers,
                                 json=ingredients)
        return [response.status_code, response.json()]



