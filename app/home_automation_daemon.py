from thermostat import Thermostat
from switch import Switch
from time import sleep
import config


def main():
    thermostat = Thermostat(
        config.api_base_path,
        config.api_token,
        config.home_thermostat_id
    )

    temp_automation_switch = Switch(
        config.api_base_path,
        config.api_token,
        config.home_temp_automation_switch
    )

    while True:
        current_temp, min_temp, max_temp = thermostat.getTempStatuses()
        if min_temp > max_temp or temp_automation_switch.is_off():
            pass
        elif (current_temp < min_temp - 1):
            thermostat.setModeHeat()
        elif current_temp > max_temp + 1:
            thermostat.setModeCool()

        sleep(30)


if __name__ == '__main__':
    main()
