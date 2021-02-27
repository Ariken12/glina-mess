import serial
import time


class SerialTalk:
    def __init__(self, port):
        self.ser = serial.Serial()

        self.ser.baudrate = 9600
        self.ser.port = port

        print("Opening port %s" % port)
        try:
            self.ser.open()
            time.sleep(3)
        except:
            print("Wrong port name: reopen pls")

        print("Opened:", self.ser.is_open)

    def reopen(self, port):
        self.ser.port = port
        try:
            self.ser.open()
        except:
            print("Wrong port name: reopen pls")

    def close(self):
        if self.ser.is_open:
            self.ser.close()
        else:
            print("Open first")

        print("Closed:", not self.ser.is_open)

    def send_message(self, message):
        if self.ser.is_open:
            self.ser.write(bytes(message, 'utf-8'))
        else:
            print("Open first")
            print("Message: ", message, end='')


ser = SerialTalk('/dev/cu.usbserial-1460')
for j in range(20):
    for i in range(3):
        command = 'x -200 y -200\n'
        ser.send_message(command)
        time.sleep(4)

        command = 'x 200 y 200\n'
        ser.send_message(command)
        time.sleep(4)

    command = 'x 0 y 1000\n'
    ser.send_message(command)
    time.sleep(10)

    for i in range(3):
        command = 'x -200 y -200\n'
        ser.send_message(command)
        time.sleep(4)

        command = 'x 200 y 200\n'
        ser.send_message(command)
        time.sleep(4)

    command = 'x 0 y -1000\n'
    ser.send_message(command)
    time.sleep(10)


ser.close()
