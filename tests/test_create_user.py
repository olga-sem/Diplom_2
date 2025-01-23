import allure
from data import EXISTING_USER, NOT_ALL_FIELDS
from methods.create_user import CreateUser


class TestCreateUSer:
    @allure.title('Тест на регистрацию нового пользователя с валидными данными')
    @allure.description('Проверяем регистрацию пользователя с валидными данными')
    def test_create_new_user(self, create_and_delete_user):
        user = CreateUser().create_new_user(create_and_delete_user)

        assert user[0] == 200 and 'accessToken' in user[1]

    @allure.title('Тест на регистрацию нового пользователя с существующими данными')
    @allure.description('Проверяем невозможность зарегистрировать пользователя с существующими данными')
    def test_create_user_with_existing_data(self, create_and_delete_user):
        CreateUser().create_new_user(create_and_delete_user)
        user_1 = CreateUser().create_new_user(create_and_delete_user)

        assert user_1[0] == 403 and user_1[1] == EXISTING_USER

    @allure.title('Тест на регистрацию нового пользователя с незаполенным обязательным полем')
    @allure.description('Проверяем невозможность зарегистрировать пользователя без заполнения обязательного поля Пароль')
    def test_create_user_without_password(self, create_and_delete_user):
        payload = {
            "email": create_and_delete_user["email"],
            "password": "",
            "name": create_and_delete_user["name"]
        }
        user = CreateUser().create_new_user(payload)

        assert user[0] == 403 and user[1] == NOT_ALL_FIELDS