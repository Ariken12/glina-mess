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
