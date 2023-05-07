# localhost
IP = '127.0.0.1'
# dict PORTS | server_id : port
PORTS = {1: 6041,
         2: 6042,
         3: 6043,
         4: 6044,
         5: 6045}
# dict servers_ips | server_id : str(server_full_ip)
servers_ips = {1: IP + str(PORTS[1]),
               2: IP + str(PORTS[2]),
               3: IP + str(PORTS[3]),
               4: IP + str(PORTS[4]),
               5: IP + str(PORTS[5])}
print(servers_ips)

# ------------------------------------------------------------------
# class Client:
#     def __init__(self, id, addr, socket):
#         self.id = id
#         self.addr = addr  # server_full_ip_tuple(ip, port)
#         self.socket = socket  # socket_full_ip_tuple(ip, port)
# ------------------------------------------------------------------

def hello_from_client(conn_socket, client_address):
    print("start listening from ", client_address)
    while True:
        # wait for incoming requests from specific socket
        data = conn_socket.recv(1024)  # hello

        data_decoded = data.decode()
        if data_decoded.replace(" ", "") == "":
            print("recieved from:", client_address, ', text:_', data_decoded)
        if data_decoded == "hello":
            print("got \"hello\", sending \"world\"...")
            conn_socket.send("world".encode())
            # conn_socket.close()  # close connection





threading.Thread(target=global_listener, args=()).start()