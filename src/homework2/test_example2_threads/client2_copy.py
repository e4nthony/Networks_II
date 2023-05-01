import socket

# init socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
# handshake with server
sock.connect(('127.0.0.1', 9999))  # server ip , port

print('successful connection')

while True:
    # save text to send
    data = input('Enter line:').strip().encode()
    # send
    sock.send(data)

    # receive answer from server
    reply_data = sock.recv(1024)
    print('server reply:', reply_data.decode())
