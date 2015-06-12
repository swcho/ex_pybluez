__author__ = 'sungwoo'

import dbus

system_bus = dbus.SystemBus()

bluezManager = dbus.Interface(system_bus.get_object("org.bluez", "/"), "org.bluez.Manager")
adapter_path = bluezManager.DefaultAdapter()
service = dbus.Interface(system_bus.get_object("org.bluez", adapter_path), "org.bluez.Service")
