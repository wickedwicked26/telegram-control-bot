from config import port, host, username, password
import paramiko
from telebot import types

check_process_button = types.KeyboardButton('CHECK MODULE 1')
check_process_button2 = types.KeyboardButton('CHECK MODULE 2')


def check_first_script():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, port=port, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(f"sudo systemctl status module1.service")
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode()

        process_list = stdout.read().decode().strip().split('\n')

        if process_list:
            return f'[INFO] MODULE 1 :{output}'

        else:
            return f'[INFO] SOMETHING WRONG : {error}'

    except Exception as e:

        return f'[INFO] EXCEPTION : {e}'

    finally:
        client.close()


def check_second_script():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, port=port, username=username, password=password)

        stdin, stdout, stderr = client.exec_command(f"sudo systemctl status module2.service")
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode()

        process_list = stdout.read().decode().strip().split('\n')

        if process_list:
            return f'[INFO] MODULE 2 :{output}'

        else:
            return f'[INFO] SOMETHING WRONG : {error}'

    except Exception as e:

        return f'[INFO] EXCEPTION : {e}'

    finally:
        client.close()
