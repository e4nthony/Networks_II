import socket

UDP_IP = '0.0.0.0'
UDP_PORT = 7777  # int

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

sock.bind((UDP_IP, UDP_PORT))

print('server ready.')
while True:
    data, addr = sock.recvfrom(1024)
    print('server received message:_', data.decode())
