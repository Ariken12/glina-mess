import socket as sc


def send_to_server(ip, port, data):
    sock = sc.socket()
    sock.connect((ip, port))
    print(data)
    sock.send(str(data).encode('utf-8'))
    inputs = sock.recv(1024)
    sock.close()
    return inputs.decode('utf-8')
