import socket

# port range: 1 to 65535
# port numbers 1 - 1024 are reserved for core protocols.

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print ("Connection from: " + str(addr))

    while True:
        data = c.recv(1024)
        if not data:
            break
        data = data.decode('utf-8')
        print ("from connected user: " + data)
        print ("sending: " + data)
        c.send(data.encode('utf-8'))

    c.close()

if __name__ == '__main__':
    Main()
