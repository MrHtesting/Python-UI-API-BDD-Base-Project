import configparser
from apiritif import http
from json import load
import os
from enum import Enum


class RequestType(Enum):
    GET = 1
    POST = 2
    PUT = 3
    PATCH = 4
    DELETE = 5


def load_config():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(
        ['{dir_path}/../config/api.ini'.format(dir_path=dir_path)], 'utf-8')
    return config


def load_json(site, request_file):
    json = None
    with open(f"resources/{site}/{request_file}.json") as json_file:
        json = load(json_file)
    return json


class ApiTestingClient:
    def __init__(self):
        self.response = None

    def make_request(self,
                     url,
                     request_type: RequestType,
                     json):

        # URL for the request
        address = url
        # URL params dict
        params = None
        # HTTP headers
        headers = None
        # request cookies
        cookies = None
        # raw request data
        data = None
        # attach JSON object as request body
        # json = json.get("requestBody", {})
        # certificate to use with request
        encrypted_cert = None
        # automatically follow HTTP redirects
        allow_redirects = True
        # request timeout, by default it's 30 seconds
        timeout = 30

        print("====================================================================")
        print(type(json))

        if request_type == RequestType.GET.name:
            return self.get_request(address)
        elif request_type == RequestType.POST.name:
            return self.post_request(address,
                                     json=json)
        else:
            return None

    def get_request(self, address, **kwargs):
        self.response = http.get(address, **kwargs)
        return self.response

    def post_request(self, address, **kwargs):
        self.response = http.post(address, **kwargs)
        return self.response

    def put_request(self, address, **kwargs):
        self.response = http.put(address, **kwargs)
        return self.response

    def patch_request(self, address, **kwargs):
        self.response = http.patch(address, **kwargs)
        return self.response

    def delete_request(self, address, **kwargs):
        self.response = http.delete(address, **kwargs)
        return self.response


if __name__ == "__main__":
    client = ApiTestingClient()
# print(client.get_config()["JSONPLACEHOLDER"]["BASEURL"])
