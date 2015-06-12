__author__ = 'sungwoo'

import dbus

system_bus = dbus.SystemBus()

bluezManager = dbus.Interface(system_bus.get_object("org.bluez", "/"), "org.bluez.Manager")

# Return object path for the default adapter
print 'Manager.DefaultAdapter: ', bluezManager.DefaultAdapter()

# Return object path for the default adapter
print 'Manager.GetProperties: ', bluezManager.GetProperties()

# Returns list of adapter object paths under /org/bluez
print 'Manager.ListAdapters: ', bluezManager.ListAdapters()

adapter_path = bluezManager.DefaultAdapter()
service = dbus.Interface(system_bus.get_object("org.bluez", adapter_path), "org.bluez.Service")
