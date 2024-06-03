import allure
import data
import helper
from conftest import default_courier
from samokat_api import SamokatApi
from helper import DeleteCourier


class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера')
    @allure.description('Проверка успешного создания курьера, проверка статус-кода и текста ответа')
    def test_success_create_courier(self, default_courier):
        created_courier_request, courier = default_courier

        assert created_courier_request.status_code == 201 and created_courier_request.json()['ok'] == True
        delete_response = DeleteCourier.delete_courier(courier['login'], courier['password'])
        assert delete_response.status_code == 200

    @allure.title('Проверка отсутствия возможности создания двух одинаковых курьеров')
    @allure.description('Проверка ошибки, статус-кода и текста ответа')
    def test_create_courier_duplicate(self):
        created_courier_request = SamokatApi.create_courier(data.TestDataCreateCourier.CREATE_COURIER_BODY)
        created_one_more_courier_request = SamokatApi.create_courier(data.TestDataCreateCourier.CREATE_COURIER_BODY)

        assert (created_courier_request.status_code == 409 and created_courier_request.json()['message'] ==
                data.ResponseMessages.four_hundred_nine_message
                and created_one_more_courier_request.status_code == 409
                and created_one_more_courier_request.json()['message'] ==
                data.ResponseMessages.four_hundred_nine_message)

    @allure.title('Проверка ошибки при отсутствии одного из обязательных полей')
    @allure.description('Проверка ошибки, статус-кода и текста ответа')
    def test_empty_name_create_courier(self):
        body = helper.ChangeTestDataRegistration.modify_create_courier_body(self, "login", "")
        created_courier_request = SamokatApi.create_courier(body)

        assert (created_courier_request.status_code == 400 and created_courier_request.json()['message'] ==
                data.ResponseMessages.four_hundred_massage)
