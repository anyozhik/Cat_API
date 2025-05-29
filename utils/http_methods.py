import allure
import requests
from utils.logger import Logger

"""The list of HTTP methods"""

class HttpMethods:
    headers_1 = {'x-api-key': '18e88fdf-ef0c-475a-b0f8-b944ba107814'}
    headers_2 = {'Content-Type': 'application/json', 'x-api-key': '18e88fdf-ef0c-475a-b0f8-b944ba107814'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("Method GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers = HttpMethods.headers_2, cookies = HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("Method POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json = body,  headers=HttpMethods.headers_2, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post_upload(url, files):
        with allure.step("Method POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, headers=HttpMethods.headers_1, cookies=HttpMethods.cookie, files=files)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url):
        with allure.step("Method DELETE"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, headers=HttpMethods.headers_2, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result
