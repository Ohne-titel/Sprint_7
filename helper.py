import allure
import requests
from faker import Faker
import data
import urls


class ChangeTestDataRegistration:
    @staticmethod
    @allure.step('Копия метода создания курьера для регистрации')
    def modify_create_courier_body(self, key, value):
        body = data.TestDataCreateCourier.CREATE_COURIER_BODY.copy()
        body[key] = value

        return body


class CourierGenerate:

    @staticmethod
    @allure.step('Генерация тела для регистрации курьера')
    def courier_body_with_faker():
        fake = Faker()

        return {
            "login": fake.name(),
            "password": fake.password(),
            "firstName": fake.first_name()
        }


class LoginCourierGenerate:

    @staticmethod
    @allure.step('Генерация тела для логина курьера')
    def courier_login_body_with_faker():
        fake = Faker()

        return {
            "login": fake.name(),
            "password": fake.password()
        }


class ChangeTestDataLogin:
    @staticmethod
    @allure.step('Копия создания курьера для логина')
    def modify_login_courier_body(self, key, value):
        body = data.TestLoginData.LOGIN_DATA.copy()
        body[key] = value

        return body


class DeleteCourier:
    @staticmethod
    def delete_courier(login, password):
        response = requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, data={
            "login": login,
            "password": password,
        })
        requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT + f"/{response.json()["id"]}")

        return response
