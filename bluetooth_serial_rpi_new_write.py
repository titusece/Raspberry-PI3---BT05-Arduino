#! /usr/bin/python

# should run like below
# python bluetooth_serial_rpi_new.py 2 20:16:06:12:08:89

import serial
from time import sleep
import argparse
import os
import time

parser = argparse.ArgumentParser(description="Get the count no of times to blink the Arduino IO 13")
parser.add_argument("c", type=str, help="Command/Data")
parser.add_argument("d", type=str, help="BT Device address")
args = parser.parse_args()

os.system('rfcomm bind 0 ' + args.d + ' 1')
print('rfcomm binding done...');

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )
command_data = args.c;

print('Trying to write command/data into BT device');
bluetoothSerial.write( str(command_data) )
#waiting...
time.sleep(5);

os.system('rfcomm unbind 0')
print('rfcomm unbinding done...');
