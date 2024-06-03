class TestDataCreateCourier:
    CREATE_COURIER_BODY = {
        "login": "kina",
        "password": "12344",
        "firstName": "fister"
    }


class TestLoginData:
    LOGIN_DATA = {
        "login": " jerbge",
        "password": "12434"
    }


class TestOrderData:
    ORDER_DATA = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }


class ResponseMessages:
    four_hundred_nine_message = "Этот логин уже используется. Попробуйте другой."
    four_hundred_massage = "Недостаточно данных для создания учетной записи"
    four_hundred_login_massage = "Недостаточно данных для входа"
    four_hundred_four_login_message = "Учетная запись не найдена"
