import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 7777

MESSAGE = 'Message, Hello World!'.encode()

print('UDP target IP:_ ', UDP_IP)
print('UDP target PORT:_ ', UDP_PORT)
print('message:_ ', MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
