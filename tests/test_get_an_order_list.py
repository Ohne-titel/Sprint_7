import allure
from samokat_api import SamokatApi


class TestOrderList:

    @allure.title('Проверка получения списка заказов')
    def test_get_an_order_list(self):
        order_list = SamokatApi.get_an_order_list(self)

        assert order_list.status_code == 200
        print(order_list)

