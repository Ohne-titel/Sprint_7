import allure
import pytest
from samokat_api import SamokatApi


class TestCreateOrder:
    @pytest.mark.parametrize(
        'colour',
        [
            ['BLACK'],
            ['GREY'],
            ['BLACK', 'GREY'],
            ['']
        ]
    )
    @allure.title('Проверка успешного создания заказа')
    @allure.description('Проверка успешного создания заказа c разной комбинацией данных в строке "цвет"')
    def test_success_create_order_parametrize(self, colour):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": colour
        }
        created_order = SamokatApi.create_order(payload)
        order_track = created_order.json()["track"]

        assert created_order.status_code == 201 and order_track is not None and order_track > 0
