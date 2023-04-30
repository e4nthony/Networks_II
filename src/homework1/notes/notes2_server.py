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

# Listener
while True:
    client_data, client_addr = rcv_sock.recvfrom(1024)
    if not client_data or not client_addr:
        break  # error - corrupted message
    print('server received message:_', client_data.decode(), '. from:_', client_addr)

    if client_addr not in my_clients_dict.values():
        my_clients_dict.update({client_data: client_addr})  # client_data = ClientName
        break  # done
    # elif client_addr in my_clients_dict:

    datatemp = client_data.split()
    target_name, target_msg = datatemp[0], datatemp[1]

    if not target_msg:
        break  # error - wrong format

    # init sending socket (for current target)
    snd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    message = ''

    if target_name not in my_clients_dict.values():
        print('warning, unknown target')
        snd_sock.bind(client_addr)
        message = 'unknown user name'
    else:
        print('known target. sending message')
        final_addr = my_clients_dict[target_name]
        snd_sock.bind(final_addr)
        # todo
        message = target_msg

    snd_sock.sendto(message, final_addr)
    snd_sock.close

print('server end.')
rcv_sock.close
