from Move_checker import *
from Server import *
from Checker import *

PORT = 42474
DEFAULT_IP = ['ip1', 'ip2']
IP1 = 'ip1'
IP2 = 'ip2'


def main():
    socket = Server(PORT)
    data = {'any': ['INPUT'],
            IP1: ['INPUT'],
            IP2: ['INPUT']}
    board = Checker()
    while True:
        input_data, address = socket.watch(data)
        if input_data != 'CHECK':
            print(input_data)
        input_data = input_data.split()
        address = address[0]
        if input_data[0] == 'CHECK':
            data[address].append('INPUT')
        elif input_data[0] == 'MOVE':
            if address in board.active_player:
                x1, y1 = int(input_data[1]), int(input_data[2])
                x2, y2 = int(input_data[3]), int(input_data[4])
                err = board.move(x1, y1, x2, y2, address)
                if err:
                    board.change_player()
                    for ip in data:
                        data[ip].append('OUTPUT' + ' ' + ' '.join(input_data[1:]))
                else:
                    data[address].append('ERROR wrong step')

            else:
                data[address].append('ERROR wrong player')
        elif input_data[0] == 'LOGIN':
            found = False
            need_place = True
            for i in data:
                if address == i:
                    need_place = False
                    break
            for i in data:
                if i in DEFAULT_IP and need_place:
                    data.pop(i)
                    data[address] = []
                    data[address].append('SUCCESS ' + address)
                    if board.white == (2, 4):
                        board.set_white((address, 3))
                    elif board.black == (1, 3):
                        board.set_black((address, 4))
                    found = True
                    break
            if not need_place:
                data[address].append('SUCCESS ' + address)
            if not found:
                data[address].append('ERROR cant connection')


if __name__ == "__main__":
    main()
