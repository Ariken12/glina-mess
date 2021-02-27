from GUI import *
from Client import *
import time

IP = 'ariken.ddns.net'
PORT = 42474


def main():
    gui = Window()
    ip = IP
    port = PORT
    buf = ' '
    message = ''
    last = ' '
    print('connection...')
    while 'SUCCESS' not in message:
        message = send_to_server(ip, port, 'LOGIN')
    while True:
        gui.update()
        message = send_to_server(ip, port, "CHECK").split()
        if message[0] == "INPUT":
            if gui.tap_button != last and last != ' ':
                send_to_server(ip, port,
                               'MOVE %d %d %d %d' % (last[0], last[1],
                                                     gui.tap_button[0],
                                                     gui.tap_button[1]))
                gui.tap_button = ' '
                last = ' '
            last = gui.tap_button
        elif message[0] == "OUTPUT":
            coords = list(map(int, message[1:]))
            gui.put_checker(coords[2], coords[3], gui.desk[coords[1]][coords[0]])
            gui.put_checker(coords[0], coords[1], EMPTY)
        elif message[0] == "ERROR":
            print("Error")
        time.sleep(0.033)


if __name__ == "__main__":
    main()
