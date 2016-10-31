#! /usr/bin/python

# should run like below
# python bluetooth_serial_rpi_new.py 2 20:16:06:12:08:89

import serial
from time import sleep
import argparse
import os
import time

parser = argparse.ArgumentParser(description="Get the count no of times to blink the Arduino IO 13")
parser.add_argument("c", type=int, help="Count")
parser.add_argument("d", type=str, help="BT Device address")
args = parser.parse_args()

os.system('rfcomm bind 0 ' + args.d + ' 3')
print('rfcomm binding done...');

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )
count = args.c;

print('Trying to write into BT device');
bluetoothSerial.write( str(count) )
time.sleep(5); #take some time

#print bluetoothSerial.readline()

print("Bluetooth write success!");

'''
try:
	print('Trying to write into BT device');
	bluetoothSerial.write( str(count) )
	print bluetoothSerial.readline()

except:
	os.system('rfcomm unbind 0')
	print('Failed to write, rfcomm unbinding done...');
	

os.system('rfcomm unbind 0')
print('rfcomm unbinding done...');
'''

os.system('rfcomm unbind 0')
print('rfcomm unbinding done...');
