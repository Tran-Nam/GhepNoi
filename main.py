import bluetooth
import time
from App import App
from notice import notice
import threading
# import lightblue

# need turn on blurtooth before call
# 98:D3:31:F9:40:8A
base = '98:D3:31:F9:40:8A'
"""
print("Searching device ...")
nearby_device = bluetooth.discover_devices(lookup_names=True)

while len(nearby_device)==0:
    print("Not found! Continue searching ...")
    nearby_device = bluetooth.discover_devices(lookup_names=True)

for device in nearby_device:
    addr, name = device
    # port = 1
    print("Found {} at address {}".format(name, addr))

    # only pick HC05 module
    if name=='HC05':
        break """

# if name=='HC05':
    # app = App(addr)
app = App(base)

while True:
    # show in led board

    app.send()

    
    # notice infor next patient
    b = threading.Thread(target=notice, args=())
    b.start()
    b.join()
    
    
    time.sleep(0.5)
app.close()
