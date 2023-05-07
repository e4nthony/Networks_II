# Peer To Peer (P2P) Server

import socket
import threading
import struct

# localhost
IP = '127.0.0.1'
# dict PORTS | server_id : port
PORTS = {1: 6041,
         2: 6042,
         3: 6043,
         4: 6044,
         5: 6045}
# dict s_addresses | server_id : server_full_ip_tuple(ip, port)
s_addresses = {1: (IP + PORTS[1]),
               2: (IP + PORTS[2]),
               3: (IP + PORTS[3]),
               4: (IP + PORTS[4]),
               5: (IP + PORTS[5])}
# dict clients | server_id: active_client_socket - saves clients that are online - that this server accepted
clients = dict()
# dict servers | server_id: active_servers_socket - saves servers that are online - that this client connected
servers = dict()

# init this server id and port
my_server_id = int(input("Enter id of this client [1-5]:"))
my_server_port = PORTS[my_server_id]
my_server_addr = ('0.0.0.0', my_server_port)

# make public socket for incoming requests (and handshakes)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(my_server_addr)
# listen to port assigned for my server id
sock.listen(1)

# external addresses
ext_addresses = s_addresses
ext_addresses.pop(my_server_id)


def handle_peer(client_socket, client_address):
    def get_server_id_by_port(client_port):
        """*it works ok for dict length 5"""
        key_list = list(PORTS.keys())
        val_list = list(PORTS.values())
        position = val_list.index(client_port)
        return key_list[position]

    print("a new connection with ", client_address)
    client_ip, client_port = client_address.getpeername()
    client_id = get_server_id_by_port(client_port)

    clients[client_id] = client_socket  # save to dict new client

    print("ready for incoming requests")

    while True:
        data = client_socket.recv(1024)

        type, subtype, len, sublen, msg = struct.unpack(">4i10s", data)
        msg = msg.decode().rstrip("\x00)")  # need decode string, and remove blank bytes at end of string

        if type == 0:  # Get info about connections - request
            if subtype == 0:


        elif type == 1:  # Get info about connections - request

        elif type == 3:

        elif type == 4:

        else:
            print("error: got unexpected 'type' value")

    if == "":
        print("recieved from:", client_address, ', text:_', data_decoded)
    if data_decoded == "hello":
        print("got \"hello\", sending \"world\"...")
        client_socket.send("world".encode())
        # conn_socket.close()  # close connection


def global_listener():
    print("start listening to new conn messages.")
    while True:
        # wait for incoming requests (handshakes)
        client_socket, client_address = sock.accept()
        # make a thread for this new connection
        threading.Thread(target=handle_peer, args=(client_socket, client_address).start())


threading.Thread(target=global_listener, args=()).start()

# --------- broadcast that I am online ---------


def pack_data_type1():
    """pack data for initial req"""
    type, subtype, len, sublen, msg = 1, 1, 0, 0, ""

    return struct.pack(">4i10s", type, subtype, len, sublen, msg)


# def pack_data_type2():
#     """pack data for initial req"""
#     type, subtype, len, sublen, msg = 1, 1, 0, 0, ""
#
#     data = struct.pack(">4i", type, subtype, len, sublen)
#     return

# handshake with other servers
for key, val in ext_addresses.items():
    try:
        print("trying to connect to server | id:", key, ", ip:", val)
        sock.connect(val)
        # if here then the TCP connection is established
        servers[key] = sock  # save to dict new server connection

        data = pack_data_type1()

        print("sending data: ", data)
        sock.send(data)
        #-----------------------------------

        # receive answer from server
        reply_data = outc_sock.recv(1024)
        print("got reply: \"", reply_data.decode(), "\"")
        outc_sock.close()  # close connection

        print("connection established successfully with server id: ", key)
        # break  # to eliminate connection to other
    except ConnectionRefusedError:
        print("ConnectionRefusedError at server id: ", key)
    except socket.error:
        print('Failed to reuse socket')  # todo delete

# threading.Thread(target=global_listener, args=()).start()
