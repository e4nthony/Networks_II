import socket

# init default public listening socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('0.0.0.0', 9999))  # listen port

sock.listen(1)

# when first pack arrives
conn, client_address = sock.accept()
print('new connection from', client_address)

while True:
    # when message from user arrives
    data = conn.recv(1024)
    # send echo back
    conn.send(b'Echo : ' + data)
