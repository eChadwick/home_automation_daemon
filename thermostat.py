import requests
import json


class Thermostat:
    def __init__(self, auth_token, device_id):
        self.auth_header = {'Authorization': f'Bearer {auth_token}'}
        self.api_base_path = f'https://api.smartthings.com/v1/devices/{device_id}'

    def getTempStatuses(self):
        response = requests.get(
            f'{self.api_base_path}/status',
            headers=self.auth_header,
            timeout=10
        )
        response_json = json.loads(response.text)
        current_temp = response_json['components']['main']['temperatureMeasurement']['temperature']['value']
        max_temp = response_json['components']['main']['thermostatCoolingSetpoint']['coolingSetpoint']['value']
        min_temp = response_json['components']['main']['thermostatHeatingSetpoint']['heatingSetpoint']['value']

        return current_temp, min_temp, max_temp

    def setModeCool(self):
        requests.post(
            f'{self.api_base_path}/commands',
            headers=self.auth_header,
            json={
                'commands': [
                    {
                        'component': 'main',
                        'capability': 'thermostatMode',
                        'command': 'cool',
                    }
                ]
            },
            timeout=10
        )

    def setModeHeat(self):
        requests.post(
            f'{self.api_base_path}/commands',
            headers=self.auth_header,
            json={
                'commands': [
                    {
                        'component': 'main',
                        'capability': 'thermostatMode',
                        'command': 'heat',
                    }
                ]
            },
            timeout=10
        )
