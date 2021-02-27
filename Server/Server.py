import socket as sc


class Server(sc.socket):
    def __init__(self, port):
        sc.socket.__init__(self)
        self.bind(('', port))
        self.listen()

    def watch(self, data):
        connect, address = self.accept()
        # print('Connection from ', address)
        inputs = connect.recv(1024).decode('utf-8')
        outputs = data['any'].pop() if len(data['any']) > 0 else 'INPUT'

        if address[0] in data and outputs == 'INPUT':
            outputs = str(data[address[0]].pop())
        if outputs[0] != 'I':
            print(outputs)
        connect.send(outputs.encode('utf-8'))
        connect.close()
        return inputs, address
