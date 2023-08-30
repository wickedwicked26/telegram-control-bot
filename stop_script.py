import paramiko
from telebot import types

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
        stop_command = 'pkill -f module2.py'
        stdin, stdout, stderr = client.exec_command(stop_command)
        stdin, stdout, stderr = client.exec_command(f'pgrep -af {remote_script_path}')

        process_list = stdout.read().decode().strip().split('\n')
        if process_list:
            return 'BOT WASN\'T STOPPED'
        else:
            return 'BOT STOPPED'
    except Exception as e:
        return f'SOMETHING WENT WRONG : {e}'
    finally:
        client.close()
