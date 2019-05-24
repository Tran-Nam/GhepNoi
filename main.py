import bluetooth
import time
from App import App
# from notice import notice
# import threading
# import lightblue

# need turn on blurtooth before call
# MAC HC05 : 98:D3:31:F9:40:8A
addr = '98:D3:31:F9:40:8A'
app = App(addr)

while True:
    app.send_to_show()    
    time.sleep(0.5)

