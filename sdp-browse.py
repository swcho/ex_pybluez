__author__ = 'sungwoo'

import sys
import bluetooth
import struct
import binascii

if len(sys.argv) < 2:
    print("usage: sdp-browse <addr>")
    print("   addr can be a bluetooth address, \"localhost\", or \"all\"")
    sys.exit(2)

target = sys.argv[1]
if target == "all": target = None

services = bluetooth.find_service(address=target)

if len(services) > 0:
    print("found %d services on %s" % (len(services), sys.argv[1]))
    print()
else:
    print("no services found")

for svc in services:
    print('=======================================')
    print("Service Name: %s"    % svc["name"])
    print("    Host:        %s" % svc["host"])
    print("    Port:        %s" % svc["port"])
    print("    Description: %s" % svc["description"])
    print("    Provided By: %s" % svc["provider"])
    print("    Protocol:    %s" % svc["protocol"])
    print("    channel/PSM: %s" % svc["port"])
    print("    svc classes: %s "% svc["service-classes"])
    print("    profiles:    %s "% svc["profiles"])
    print("    service id:  %s "% svc["service-id"])

    service_classes = svc["service-classes"]

    # ref: https://www.bluetooth.org/ko-kr/specification/assigned-numbers/service-discovery
    # check A/V RemoteControlTarget
    if '110C' in service_classes:
        host = svc["host"]
        port = svc["port"]

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