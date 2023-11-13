from thermostat import Thermostat
from time import sleep
import config


def main():
    thermostat = Thermostat(config.api_token, config.home_thermostat_id)
    while True:
        current_temp, min_temp, max_temp = thermostat.getTempStatuses()
        if min_temp > max_temp:
            pass
        elif current_temp < min_temp - 1:
            thermostat.setModeHeat()
        elif current_temp > max_temp + 1:
            thermostat.setModeCool()

        sleep(30)


if __name__ == '__main__':
    main()
