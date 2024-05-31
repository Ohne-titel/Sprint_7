import allure
import requests
import urls


class SamokatApi:
    @allure.step('Отправка запроса на создание курьера')
    def create_courier(data):
        response = requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=data)

        return response

    @allure.step('Отправка запроса на логин курьера')
    def login_courier(data):
        response = requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=data)

        return response

    @allure.step('Создание заказа')
    def create_order(data):
        response = requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=data)

        return response

    @allure.step('Получение списка заказов')
    def get_an_order_list(self):
        response = requests.get(urls.BASE_URL + urls.ORDER_LIST_ENDPOINT)

        return response
