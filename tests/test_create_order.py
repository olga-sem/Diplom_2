import allure
from data import NO_INGREDIENTS, WRONG_HASH
from methods.create_order import CreateOrder
from methods.auth_user import AuthUser

class TestCreateOrder:
    @allure.title('Тест на создание заказа авторизованным пользователем с указанием ингредиентов')
    @allure.description('Проверяем возможность оформить заказ с указанием ингредиентов для авторизованного пользователя')
    def test_create_order_with_authorization_and_ingredients(self, create_and_delete_user):
        auth = AuthUser().login_with_existing_data(create_and_delete_user)
        auth_response = auth[1]
        access_token = auth_response["accessToken"]
        order = CreateOrder().create_order_with_authorization_and_ingredients(access_token)

        assert order[0] == 200 and 'order' in order[1]

    @allure.title('Тест на создание заказа авторизованным пользователем без указания ингредиентов')
    @allure.description(
        'Проверяем невозможность оформить заказ без указания ингредиентов для авторизованного пользователя')
    def test_create_order_without_ingredients(self, create_and_delete_user):
        auth = AuthUser().login_with_existing_data(create_and_delete_user)
        auth_response = auth[1]
        access_token = auth_response["accessToken"]
        order = CreateOrder().create_order_without_ingredients(access_token)

        assert order[0] == 400 and order[1] == NO_INGREDIENTS

    @allure.title('Тест на создание заказа авторизованным пользователем с неправильным хешем ингредиентов')
    @allure.description(
        'Проверяем невозможность оформить заказ с неправильным хешем ингрединтов для авторизованного пользователя')
    def test_create_order_with_wrong_hash(self, create_and_delete_user):
        auth = AuthUser().login_with_existing_data(create_and_delete_user)
        auth_response = auth[1]
        access_token = auth_response["accessToken"]
        order = CreateOrder().create_order_with_wrong_hash(access_token)
        assert order[0] == 500 and WRONG_HASH in order[1]


    @allure.title('Тест на создание заказа неавторизованным пользователем')
    @allure.description('Проверяем невозможность оформить заказ для неавторизованного пользователя')
    def test_create_order_without_authorization(self):
        order = CreateOrder().create_order_without_authorization()

        assert order[0] == 200 and 'order' in order[1]