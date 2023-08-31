import os

import paramiko
from telebot import types

start_button_first_module = types.KeyboardButton("START MODULE 1")
start_button_second_module = types.KeyboardButton("START MODULE 2")


def run_remote_script_first_module():
    host = ''
    port = int()
    username = ''
    password = ''
    remote_script_path = ''
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, port=port, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(f"python main_module.py")
        output = stdout.read().decode()
        error = stderr.read().decode()
        stdin, stdout, stderr = client.exec_command(f'pgrep -af main_module.py')

        process_list = stdout.read().decode().strip().split('\n')

        if process_list:
            return 'BOT STARTED'

        else:
            return 'SOMETHING WRONG WITH CONNECTION TO SERVER'

    except Exception as e:

        return f'BOT IS WORKING'
    finally:
        client.close()


def run_remote_script_second_module():
    host = ''
    port = int()
    username = ''
    password = ''
    remote_script_path = ''
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, port=port, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(f"python module2.py")
        output = stdout.read().decode()
        error = stderr.read().decode()
        stdin, stdout, stderr = client.exec_command(f'pgrep -af module2.py')

        process_list = stdout.read().decode().strip().split('\n')

        if process_list:
            return 'MODULE 2 STARTED'

        else:
            return 'SOMETHING WRONG WITH CONNECTION TO SERVER'

    except Exception as e:
        return f'BOT IS WORKING'
    finally:
        client.close()
