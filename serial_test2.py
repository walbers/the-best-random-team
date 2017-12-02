#blinks an led?
#need to install libraries
#https://diyhacking.com/connect-interface-raspberry-pi-arduino/

import serial
import time

ser = serial.Serial(
port = '/dev/ttyACM0',
baudrate = 9600,
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
bytesize = serial.EIGHTBITS,
timeout = 3
)
ser.open()

#LEDs On
read_ser=ser.readline()
print(read_ser)
print('sending on')
print(ser.write('on'.encode('utf-8')))

#Wait
time.sleep(1)
read_ser=ser.readline()
print(read_ser)

#LEDs Off
print('sending off')
print(ser.write('off'.encode('utf-8')))
read_ser=ser.readline()
print(read_ser)