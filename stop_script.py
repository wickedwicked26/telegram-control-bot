import paramiko
from telebot import types
import os

stop_button = types.KeyboardButton("STOP BOT")


def stop_remote_script():
    host = ''
    port = int()
    username = ''
    password = ''
    remote_script_path = ''

    client = paramiko.SSHClient()
    try:
        client.connect(hostname=host, username=username, password=password)

        stop_command = 'pkill -f main_module.py'
        stdin, stdout, stderr = client.exec_command(stop_command)
        stdin, stdout, stderr = client.exec_command(f'pgrep -af main_module.py')

        process_list = stdout.read().decode().strip().split('\n')

        stop_command2 = 'pkill -f module2.py'
        stdin2, stdout2, stderr2 = client.exec_command(stop_command2)
        stdin2, stdout2, stderr2 = client.exec_command(f'pgrep -af module2.py')

        process_list2 = stdout2.read().decode().strip().split('\n')
        if process_list2 and process_list2:
            return 'BOT WASN\'T STOPPED'
        else:
            return 'BOT STOPPED'
    except Exception as e:
        os.system('pkill -f main_module.py')
        os.system('pkill -f module2.py')
        # return f'SOMETHING WENT WRONG : {e}'
        return f'BOT WAS STOPPED {os.system("pkill -f module2.py")}'

    finally:
        client.close()
