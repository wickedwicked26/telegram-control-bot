from config import port, host, username, password
import paramiko
from telebot import types

start_button_first_module = types.KeyboardButton("START MODULE 1")
start_button_second_module = types.KeyboardButton("START MODULE 2")



def run_remote_script_first_module():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, port=port, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(f"sudo systemctl start module1.service")
        output = stdout.read().decode()
        error = stderr.read().decode()

        process_list = stdout.read().decode().strip().split('\n')

        if process_list:
            return f'[INFO] MODULE 1 is starting...'

        else:
            return f'[INFO] SOMETHING WRONG : {error}'

    except Exception as e:

        return f'[INFO] EXCEPTION : {e}'

    finally:
        client.close()


def run_remote_script_second_module():
    remote_script_path = ''
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, port=port, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(f"sudo systemctl start module2.service")
        output = stdout.read().decode()
        error = stderr.read().decode()

        process_list = stdout.read().decode().strip().split('\n')

        if process_list:
            return f'[INFO] MODULE 2 is starting...'

        else:
            return f'[INFO] SOMETHING WRONG : {error}'

    except Exception as e:

        return f'[INFO] EXECPTIOM : {e}'

    finally:
        client.close()
