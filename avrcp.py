__author__ = 'sungwoo'

import sys
import bluetooth
import struct
import binascii

host = 'D0:57:85:16:b1:CB'
port = 23

print 'AVRCP', host, ':', port
sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)
sock.connect((host, port))
print "connected to ", host, port

values = (0x01, 0x90, 0x00, 0x00, 0x19, 0x58, 0x10, 0x00, 0x00, 0x01, 0x01)
packer = struct.Struct('B B B B B B B B B B B')
packed_data = packer.pack(*values)

sock.send(packed_data)
data = sock.recv(1024)
print "received [%s]" % data
sock.close()