import allure
from data import FAILURE_FOR_UNAUTHORISED_USER
from methods.auth_user import AuthUser
from methods.get_certain_orders import CertainOrders


class TestCertainOrders:
    @allure.title('Тест на получение списка заказов конкретного авторизованного пользователя')
    @allure.description('Проверяем возможность получить список заказов конкретного авторизованного пользователя')
    def test_get_orders_of_certain_authorised_user(self, create_and_delete_user):
        auth = AuthUser().login_with_existing_data(create_and_delete_user)
        auth_response = auth[1]
        access_token = auth_response["accessToken"]
        orders = CertainOrders().get_orders_of_certain_authorised_user(access_token)

        assert orders[0] == 200 and 'orders' in orders[1]

    @allure.title('Тест на получение списка заказов неавторизованного пользователя')
    @allure.description('Проверяем невозможность получить список заказов неавторизованного пользователя')
    def test_get_orders_of_unauthorised_user(self):
        orders = CertainOrders().get_orders_of_unauthorised_user()

        assert orders[0] == 401 and orders[1] == FAILURE_FOR_UNAUTHORISED_USER