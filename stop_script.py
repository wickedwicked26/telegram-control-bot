from config import port, host, username, password
import paramiko
import subprocess


def stop_remote_script():
	# client = paramiko.SSHClient()
	# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		command = "sudo systemctl stop module1.service ; sudo systemctl stop module2.service"

		result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
								text=True)
		# client.connect(hostname=host, port=port, username=username, password=password)
		#
		# stdin, stdout, stderr = client.exec_command(f"sudo systemctl stop module1.service")
		# output = stdout.read().decode()
		# error = stderr.read().decode()
		#
		# process_list = stdout.read().decode().strip().split('\n')
		#
		# stdin2, stdout2, stderr2 = client.exec_command(f"sudo systemctl stop module2.service")
		# error = stdout2.read().decode()
		# process_list2 = stdout2.read().decode().strip().split('\n')
		#
		# if process_list:
		return f'[INFO] BOT STOPPED'
		#
		# else:
		# 	return f'[INFO] SOMETHING WRONG : {error}'

	except Exception as e:

		return f'[INFO] EXCEPTION : {e}'
