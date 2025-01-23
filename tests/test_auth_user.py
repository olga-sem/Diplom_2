import allure
from data import WRONG_DATA
from methods.auth_user import AuthUser


class TestAuthUser:
    @allure.title('Тест на авторизацию пользователя с валидными данными')
    @allure.description('Проверяем авторизацию пользователя с валидными данными')
    def test_login_with_existing_data(self, create_and_delete_user):
        user = AuthUser().login_with_existing_data(create_and_delete_user)

        assert user[0] == 200 and 'accessToken' in user[1]

    @allure.title('Тест на авторизацию пользователя с неверной почтой')
    @allure.description('Проверяем авторизацию пользователя с неверной почтой')
    def test_login_with_wrong_email(self):
        user = AuthUser().login_with_wrong_email('blur@gmail.com')

        assert user[0] == 401 and user[1] == WRONG_DATA

    @allure.title('Тест на авторизацию пользователя с неверным паролем')
    @allure.description('Проверяем авторизацию пользователя с неверным паролем')
    def test_login_with_wrong_password(self):
        user = AuthUser().login_with_wrong_password('qwerty123')

        assert user[0] == 401 and user[1] == WRONG_DATA