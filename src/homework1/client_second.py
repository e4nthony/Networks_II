import socket
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 9999

MESSAGE = 'arthur'.encode()

print('UDP target IP:_ ', UDP_IP)
print('UDP target PORT:_ ', UDP_PORT)
print('message:_ ', MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

# ---
time.sleep(10)

MESSAGE = 'alise helloalise'.encode()
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))