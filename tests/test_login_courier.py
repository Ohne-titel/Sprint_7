import allure
import data
import helper
from samokat_api import SamokatApi
from conftest import default_login_courier


class TestLoginCourier:
    @allure.title('Проверка успешного логина')
    @allure.description('Проверка успешного логина, статус-кода и наличие id')
    def test_success_login(self):
        response = SamokatApi.login_courier(data.TestLoginData.LOGIN_DATA)
        response_id = response.json()["id"]

        assert response.status_code == 200 and response_id is not None and response_id > 0

    @allure.title('Проверка ошибки логина при отсутствии одного из обязательных полей')
    @allure.description('Проверка ошибки логина, статус-кода и текста сообщения')
    def test_empty_password_login(self):
        body = helper.ChangeTestDataLogin.modify_login_courier_body(self, "password", "")
        logged_in_courier_request = SamokatApi.login_courier(body)

        assert (logged_in_courier_request.status_code == 400 and logged_in_courier_request.json()['message'] ==
                data.ResponseMessages.four_hundred_login_massage)

    @allure.title('Проверка ошибки логина при неверном указании пароля')
    @allure.description('Проверка ошибки логина, статус-кода и текста сообщения')
    def test_wrong_password_login(self):
        body = helper.ChangeTestDataLogin.modify_login_courier_body(self, "password", "23456")
        logged_in_courier_request = SamokatApi.login_courier(body)

        assert (logged_in_courier_request.status_code == 404 and logged_in_courier_request.json()['message'] ==
                data.ResponseMessages.four_hundred_four_login_message)

    @allure.title('Проверка ошибки логини с несуществующей учеткой')
    @allure.description('Проверка ошибки логина, статус-кода и текста сообщения')
    def test_not_existed_courier_login(self, default_login_courier):
        not_existed_courier = default_login_courier

        assert (not_existed_courier.status_code == 404 and not_existed_courier.json()['message'] ==
                data.ResponseMessages.four_hundred_four_login_message)
