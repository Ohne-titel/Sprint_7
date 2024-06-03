import allure
import pytest
from samokat_api import SamokatApi
from helper import CourierGenerate, LoginCourierGenerate


@pytest.fixture(scope='function')
@allure.step('Создание шаблонного курьера')
def default_courier():
    generated_stuff = CourierGenerate.courier_body_with_faker()
    response = SamokatApi.create_courier(generated_stuff)
    return response, generated_stuff


@pytest.fixture(scope='function')
@allure.step('Создание шаблонного курьера для логина')
def default_login_courier():
    response = SamokatApi.login_courier(LoginCourierGenerate.courier_login_body_with_faker())
    return response
