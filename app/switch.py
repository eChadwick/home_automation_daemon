import requests
import json


class Switch:
    def __init__(self, api_base_path, auth_token, device_id):
        self.auth_header = {'Authorization': f'Bearer {auth_token}'}
        self.api_base_path = f'{api_base_path}/{device_id}'

    def is_on(self):
        response = requests.get(
            f'{self.api_base_path}/status',
            headers=self.auth_header,
            timeout=10
        )
        response_json = json.loads(response.text)

        return response_json['components']['main']['switch']['switch']['value'] == 'on'

    def is_off(self):
        response = requests.get(
            f'{self.api_base_path}/status',
            headers=self.auth_header,
            timeout=10
        )
        response_json = json.loads(response.text)

        return response_json['components']['main']['switch']['switch']['value'] == 'off'
