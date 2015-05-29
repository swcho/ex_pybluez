__author__ = 'sungwoo'

import bluetooth

target_name = "My Phone"
target_address = None

nearby_devices = bluetooth.discover_devices()

print nearby_devices

for bdaddr in nearby_devices:
    device_name = bluetooth.lookup_name( bdaddr )
    print bdaddr, device_name
    if target_name == device_name:
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with address ", target_address
else:
    print "could not find target bluetooth device nearby"

