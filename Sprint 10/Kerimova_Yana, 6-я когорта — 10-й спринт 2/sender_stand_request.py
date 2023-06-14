import configuration
import requests
import data


def post_new_user(body):  # запрос на создание нового пользователя
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


def post_new_kit(kit_body, auth_token): # запрос на создание нового набора
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json=kit_body,
                         headers=headers)
