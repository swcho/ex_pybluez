__author__ = 'sungwoo'

import struct
import binascii

values = (0x01, 0x90, 0x00, 0x00, 0x19, 0x58, 0x10, 0x00, 0x00, 0x01, 0x01)
packer = struct.Struct('B B B B B B B B B B B')
packed_data = packer.pack(*values)
print binascii.hexlify(packed_data)
