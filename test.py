import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)

def passe(monInput):
	ser.write(monInput)
	print(monInput)
