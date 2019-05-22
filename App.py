import bluetooth
from convert import convert
import os

class App(object):

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    def __init__(self, addr, port=1):
        self.addr = addr
        self.port = port 
        self.sock.connect((self.addr, self.port))
    
    def send(self, text):
        text = convert(text)
        data = '1' + text + ' '
        self.sock.send(data)
        print('Sent {}'.format(text))
    
    # use file G.txt as input to send it to board 
    def send_to_show(self, path='data', filename='G.txt'):

        if filename in os.listdir(path):

            # reach content to show
            abs_path = os.path.join(path, filename)
            content = open(abs_path, 'r').read()
            content = convert(content)

            if content is None or content == "":
                return

            # empty file
            with open(abs_path, 'w') as f:
                f.write("")
            
            self.sock.send(content)
            print('Send successful!', content)

    def close(self):
        self.sock.close()
