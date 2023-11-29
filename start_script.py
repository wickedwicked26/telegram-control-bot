from config import port, host, username, password
import paramiko
import subprocess


def run_remote_script():
	# client = paramiko.SSHClient()
	# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		command = "sudo systemctl start module1.service ; sudo systemctl start module2.service"

		result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
								text=True)

		# client.connect(hostname=host, port=port, username=username, password=password)
		#
		# stdin, stdout, stderr = client.exec_command(
		# 	f"sudo systemctl start module1.service ; sudo systemctl start module2.service")
		#
		# output = stdout.read().decode()
		# error = stderr.read().decode()
		#
		# process_list = stdout.read().decode().strip().split('\n')
		#
		# if process_list:
		return f'[INFO] BOT  IS starting...'
		#
		# else:
		# 	return f'[INFO] SOMETHING WRONG : {error}'

	except Exception as e:

		return f'[INFO] EXCEPTION : {e}'
