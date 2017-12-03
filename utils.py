import serial
import time

PORT = "/dev/ttyACM0"
BAUD_RATE = 9600
PARITY = serial.PARITY_NONE
STOPBITS = serial.STOPBITS_ONE
BYTESIZE = serial.EIGHTBITS
TIMEOUT = 3

def initialize_serial():
    ser = serial.Serial(port=PORT, parity=PARITY, stopbits=STOPBITS, bytesize=BYTESIZE, timeout=TIMEOUT)
    return ser


def send_string(string):
    try:
        ser = initialize_serial()
        if not ser.isOpen():
            ser.open()
        print(ser.readline())
        print("Sending %s" % string)
        ser.write(string.encode("utf-8"))
        time.sleep(1)
        print(ser.readline())
    except Exception as e:
        print(e)
        return False
    return True
