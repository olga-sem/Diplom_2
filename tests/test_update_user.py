import allure
import helpers
from data import (FAILURE_FOR_UNAUTHORISED_USER)
from methods.auth_user import AuthUser
from methods.update_user import UpdateUser


class TestUpdateUser:
    @allure.title('Тест на обновление данных авторизованного пользователя')
    @allure.description('Проверяем возможность обновить данные авторизованного пользователя')
    def test_update_users_data_with_authorization(self, create_and_delete_user):
        auth = AuthUser().login_with_existing_data(create_and_delete_user)
        response = auth[1]
        access_token = response["accessToken"]
        new_data = helpers.create_data_for_update()
        user = UpdateUser().update_data_with_authorization(new_data, access_token)

        assert user[0] == 200 and 'success' in user[1]

    @allure.title('Тест на обновление данных неавторизованного пользователя')
    @allure.description('Проверяем невозможность обновить данные неавторизованного пользователя')
    def test_update_users_data_without_authorization(self):
        new_data = helpers.create_data_for_update()
        user = UpdateUser().update_data_without_authorization(new_data)

        assert user[0] == 401 and user[1] == FAILURE_FOR_UNAUTHORISED_USER

