import RouteBuilder
import serial_send
import time

PORT_NAME = '/dev/cu.usbserial-1460'


def move_checkers(startx, starty, endx, endy):
    rb = RouteBuilder.RouteBuilder()
    ss = serial_send.SerialTalk(PORT_NAME)
    for x in rb.build_root(startx, starty, endx, endy):
        print(x)
        a = x.split()
        if len(a) > 2:
            a[1], a[3] = abs(int(a[1])), abs(int(a[3]))
            ss.send_message(x)
            time.sleep(max(a[3], a[1]) * 0.005)
        else:
            ss.send_message(x)
            time.sleep(0.5)
