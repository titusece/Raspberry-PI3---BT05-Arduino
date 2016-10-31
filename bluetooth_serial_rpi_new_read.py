#! /usr/bin/python

# should run like below
# python bluetooth_serial_rpi_new.py 20:16:06:12:08:89

import serial
from time import sleep
import argparse
import os

parser = argparse.ArgumentParser(description="Get the count no of times to blink the Arduino IO 13")
parser.add_argument("d", type=str, help="BT Device address")
args = parser.parse_args()

os.system('rfcomm bind 1 ' + args.d + ' 1')
#print('rfcomm binding done...');

bluetoothSerial = serial.Serial( "/dev/rfcomm1", baudrate=9600 );

#print('Trying to read into BT device');
#print bluetoothSerial.readline();


try:
	print('Trying to read into BT device');
	bluetoothSerial.readline();

except:
	os.system('rfcomm unbind 1');
	print('Failed to read, rfcomm unbinding done...');

	
os.system('rfcomm unbind 1');
print('rfcomm unbinding done...');
