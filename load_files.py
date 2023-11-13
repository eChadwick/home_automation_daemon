from time import sleep
from scp import SCPClient
from paramiko import SSHClient
app_files = [
    'app/requirements.txt',
    'app/config.py',
    'app/home_automation_daemon.py',
    'app/thermostat.py',
    'app/switch.py'
]
systemd_service_file = 'app/home_automation_daemon.service'

target_app_path = '/home/pi/home_automation_daemon'
target_systemd_path = '/etc/systemd/system'


with SSHClient() as client:
    client.load_system_host_keys()
    client.connect('raspberrypi', username='root')
    client.exec_command(f'mkdir {target_app_path}')

    with SCPClient(client.get_transport()) as scp:
        print('Loading files')
        scp.put(app_files, remote_path=target_app_path)
        scp.put(systemd_service_file, remote_path=target_systemd_path)

    print('Initializing virtual environment on target')
    stdin, stdout, stderr = client.exec_command(
        f'cd {target_app_path};python3 -m venv .venv')
    stdout.channel.recv_exit_status()

    print('Installing dependencies')
    stdin, stdout, stderr = client.exec_command(
        f'cd {target_app_path}; .venv/bin/pip install -r requirements.txt')
    stdout.channel.recv_exit_status()

    print('Modifying file permissions')
    client.exec_command(
        f'chown -R home_automation_daemon:home_automation_daemon {target_app_path}')

    print('Restarting deamon')
    client.exec_command('systemctl daemon-reload')
    client.exec_command('systemctl restart home_automation_daemon')

    print('Done')
