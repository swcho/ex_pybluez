
# Examples and trials for pybluez

refs

http://karulis.github.io/pybluez/
http://people.csail.mit.edu/albert/bluez-intro/c212.html
https://android.googlesource.com/platform/packages/apps/Bluetooth/+/jb-mr2-release/src/com/android/bluetooth/a2dp/Avrcp.java
http://www.robertprice.co.uk/robblog/2007/01/programming_bluetooth_using_python-shtml/
https://github.com/Mqrius/BluePloverPi

/etc/bluetooth/main.conf
```
# Default device class. Only the major and minor device class bits are
# considered.
#Class = 0x000100
Class = 0x002540
```

file:///etc/bluetooth/audio.conf
```
# If we want to disable support for specific services
# Defaults to supporting all implemented services
Disable=Gateway,Source,Socket
```

