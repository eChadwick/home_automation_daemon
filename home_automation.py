from thermostat import Thermostat

token = '27bf5015-2ece-4d04-aa5d-1203e769a24b'
api_base_path = 'https://api.smartthings.com/v1'

location_id = 'c7ca30e9-7c19-4a16-8fa7-913cba11cdff'
thermostat_id = '61e0282f-f6ee-4503-8784-e90c255514c0'


def main():
    thermostat = Thermostat(token,thermostat_id)
    current_temp, min_temp, max_temp = thermostat.getTempStatuses()
    x=5

if __name__ == '__main__':
    main()
