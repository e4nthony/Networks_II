from threading import Thread
import socket

# init server values
UDP_IP = '0.0.0.0'
UDP_PORT = 9999  # int
server_addr = (UDP_IP, UDP_PORT)

# {name: address}
my_clients_dict = {}

# init Receiving socket (public)
rcv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
rcv_sock.bind(server_addr)

print('server ready.')

def app():
    # read incoming data
    client_data, client_addr = rcv_sock.recvfrom(1024)
    if not client_data or not client_addr:
        return  # error - corrupted message
    client_data = client_data.decode()
    print('server received message:_', client_data, '. from:_', client_addr)

    if client_addr not in my_clients_dict.values():
        my_clients_dict.update({client_data: client_addr})  # client_data = ClientName
        return  # done
    # elif client_addr in my_clients_dict:

    datatemp = client_data.split(' ', 1)
    target_name, target_msg = datatemp[0], datatemp[1]

    if not target_msg:
        return  # error - wrong format

    # init sending socket (for current target)
    snd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    message = ''

    if target_name not in my_clients_dict:
        print('warning, unknown target')
        final_addr = client_addr
        snd_sock.bind(final_addr)
        message = 'unknown user name'.encode()
    else:
        print('known target. sending message')
        final_addr = my_clients_dict[target_name]
        snd_sock.bind(final_addr)
        message = target_msg.encode()

    snd_sock.sendto(message, final_addr)
    snd_sock.close

# Listener
while True:
    app()

print('server end.')
rcv_sock.close
