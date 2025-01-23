import allure
import requests
import urls


class CertainOrders:

    @allure.step('Метод для получения списка заказов конкретного авторизованного пользователя')
    def get_orders_of_certain_authorised_user(self, access_token):
        headers = {"Authorization": access_token}
        response = requests.get(f'{urls.BASE_URL}{urls.CERTAIN_ORDERS_URL}',
                                headers=headers)
        return [response.status_code, response.json()]

    @allure.step('Метод для получения списка заказов неавторизованного пользователя')
    def get_orders_of_unauthorised_user(self):
        response = requests.get(f'{urls.BASE_URL}{urls.CERTAIN_ORDERS_URL}')
        return [response.status_code, response.json()]