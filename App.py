import bluetooth
from convert import convert
import os

class App(object):

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    def __init__(self, addr, port=1):
        self.addr = addr
        self.port = port 
        print(self.addr, self.port)
        self.sock.connect((self.addr, self.port))
        print("Connected!")
    
    def send_content(self, text):
        print('c')
        text = convert(text)
        data = '1' + text + ' '
        print('b')
        self.sock.send(data)
        print('Sent {}'.format(data))
    
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
            
            self.send_content(content)
            # print('a')
            # print('Send successful!', content)

    def close(self):
        self.sock.close()
