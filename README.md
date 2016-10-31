# Raspberry-PI3---BT05-Arduino
Control the Arduino IOs from Raspberry PI3 via BT


1) Get the channel number of your raspberry pi bluetooth.

sdptool records <MAC ID of BT>

Ex:

sdptool records 20:16:06:12:08:89

2) Run the code with channel no and MAC ID of BT.

sudo python bluetooth_serial_rpi_new.py <data> <MAC ID>

Ex:

sudo python bluetooth_serial_rpi_new.py 2 20:16:06:12:08:89



Use any one of the python scripts to communicate between BT05 device from raspberry pi3 board.
