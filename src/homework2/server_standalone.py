import socket
import threading

others_servers_ip = '127.0.0.1'
available_ids = [0, 1, 2, 3, 4]
available_ports = ["4040", "4041", "4042", "4043", "4044"]

# init this server id and port
my_server_id = int(input("enter id of server [0-4]:"))
my_server_port = int(available_ports[my_server_id])

# make public socket for incoming requests (and handshakes)
public_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
# public_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# listen to port assigned for my server index
public_sock.bind(('0.0.0.0', my_server_port))
public_sock.listen(1)


# def echo_to_client(conn_socket, client_address):
#     print("start listening from ", client_address)
#     while True:
#         # wait for incoming requests from specific socket
#         data = conn_socket.recv(1024)
#         print("recieved from", client_address, 'text', data.decode())
#         conn_socket.send(b'Echo : ' + data)


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


def global_listener():
    print("start listening to new conn messages.")
    while True:
        # wait for incoming requests (handshakes)
        conn, client_address = public_sock.accept()
        print("new connection from", client_address)

        # todo save user

        # make a thread for this new connection
        threading.Thread(target=hello_from_client, args=(conn, client_address)).start()


threading.Thread(target=global_listener, args=()).start()

# --------- broadcast that I am online ---------
other_servers_ids = available_ids
other_servers_ids.pop(my_server_id)

# init sending socket for out-coming requests
# outc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
# outc_sock.bind(('0.0.0.0', int(out_ports[my_server_id])))

# handshake with other servers
for x in other_servers_ids:
    try:
        # outc_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # make socket reusable
        # outc_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        outc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        print("trying to connect to server | id:", x, ", ip:", others_servers_ip, available_ports[x])
        outc_sock.connect((others_servers_ip, int(available_ports[x])))  # server ip str, port int
        # if here then the TCP connection is established

        print("sending \"hello\"")
        outc_sock.send("hello".encode())

        # receive answer from server
        reply_data = outc_sock.recv(1024)
        print("got reply: \"", reply_data.decode(), "\"")
        outc_sock.close()  # close connection

        print("connection established successfully with server id: ", x)
        # break  # to eliminate connection to other
    except ConnectionRefusedError:
        print("ConnectionRefusedError at server id: ", x)
    except socket.error:
        print('Failed to reuse socket')  # todo delete
