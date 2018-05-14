import socket
import time

host = '127.0.0.1'
port = 5000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0) # set it as non-blocking

quit = False
print ('Server Started')

while not quit:
	try:
		data, addr = s.recvfrom(1024)
		if 'Quit' in str(data):
			quit = True
		if addr not in clients:
			clients.append(addr)
		print (time.ctime(time.time()) + " " + data.decode('utf-8'))
		for client in clients:
			s.sendto(data.decode('utf-8'), client)
	except:
		time.sleep(0.1)
s.close()
