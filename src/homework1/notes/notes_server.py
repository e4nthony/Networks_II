from threading import Thread
import socket

# init server values
UDP_IP = '0.0.0.0'
UDP_PORT = 9999  # int
server_addr = (UDP_IP, UDP_PORT)


clients_list = list()

def output_recvfrom(clients_list, client_data, client_addr):
    while True:
        print('server received message:_', client_data.decode(),
              '\nfrom:_', client_addr)

        # init new socket for new client (private)
        c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        c_sock.bind(server_addr)

        client = {'addr': client_addr, 'socket': sock}
        clients_list.append(client)

        c_sock.sock.bind(client_addr)



# init Receiving socket (public)
rcv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
rcv_sock.bind(server_addr)

# Listener
while True:
    client_data, client_addr = rcv_sock.recvfrom(1024)
    if not client_data or not client_addr:
        break
    t = Thread(target=output_recvfrom, args=(clients_list, client_data, client_addr))
    t.start()

print('server ready.')

