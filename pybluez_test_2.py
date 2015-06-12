__author__ = 'sungwoo'
#http://pybluez.googlecode.com/svn-histor/www/docs-0.7/index.html

import sys
import bluetooth
import pprint
import Tkinter as tk
import keymap

pp = pprint.PrettyPrinter(indent=4)

# http://stackoverflow.com/questions/22688375/writing-hid-service-with-pybluez

server_sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)
server_sock.bind(("", 23))
server_sock.listen(1)

# interrupt_sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)
# interrupt_sock.bind(("", 19))
# interrupt_sock.listen(1)

bluetooth.advertise_service(
    sock=server_sock,
    name='AVRCP Emulator',
    service_classes=[bluetooth.AV_REMOTE_CLASS],
    profiles=[bluetooth.AV_REMOTE_PROFILE]
)

services = bluetooth.find_service(address='localhost')
client_sock = None
for s in services:
    pp.pprint(s)

def send_input(ir):
    #  Convert the hex array to a string
    hex_str = ""
    for element in ir:
        if type(element) is list:
            # This is our bit array - convrt it to a single byte represented
            # as a char
            bin_str = ""
            for bit in element:
                bin_str += str(bit)
            hex_str += chr(int(bin_str, 2))
        else:
            # This is a hex value - we can convert it straight to a char
            hex_str += chr(element)
    # Send an input report
    client_sock.send(hex_str)

def onKeyPress(event):
    print 'You pressed ', event.keycode, event.state, event.char, event.keysym, event.keysym_num
    scan_code = keymap.keytable['KEY_' + event.keysym.upper()]
    print 'scan code ', scan_code
    # http://cdn.sparkfun.com/datasheets/Wireless/Bluetooth/RN-HID-User-Guide-v1.0r.pdf
    state = [
        0xA1, # This is an input report
        0x01, # Usage report = Keyboard
        # Bit array for Modifier keys
        [0,   # Right GUI - (usually the Windows key)
         0,   # Right ALT
         0,   # Right Shift
         0,   # Right Control
         0,   # Left GUI - (again, usually the Windows key)
         0,   # Left ALT
         0,   # Left Shift
         0],   # Left Control
        0x00,  # Vendor reserved
        scan_code,  # Rest is space for 6 keys
        0,
        0x00,
        0x00,
        0x00,
        0x00]
    send_input(state)
    state = [
        0xA1, # This is an input report
        0x01, # Usage report = Keyboard
        # Bit array for Modifier keys
        [0,   # Right GUI - (usually the Windows key)
         0,   # Right ALT
         0,   # Right Shift
         0,   # Right Control
         0,   # Left GUI - (again, usually the Windows key)
         0,   # Left ALT
         0,   # Left Shift
         0],   # Left Control
        0x00,  # Vendor reserved
        0x00,  # Rest is space for 6 keys
        0x00,
        0x00,
        0x00,
        0x00,
        0x00]
    send_input(state)

print("Waiting for connection on L2CAP")

try:
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)
    (address, port) =  client_info
    services = bluetooth.find_service(address=address)
    for s in services:
        pp.pprint(s)

    # client_sock, client_info = interrupt_sock.accept()
    # print("Accepted interrupt connection from ", client_info)

    root = tk.Tk()
    root.geometry('300x200')
    text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
    text.pack()
    root.bind('<KeyPress>', onKeyPress)
    root.mainloop()

    while True:
        data = client_sock.recv(1024)
        if len(data) == 0:
            break
        print("received [%s]" % data)
except IOError:
    pass
except KeyboardInterrupt:
    print "Stopping..."
    bluetooth.stop_advertising(server_sock)
    sys.exit()

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")