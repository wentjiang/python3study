import socket
import threading

PORT = 9876

class ChatClient(threading.Thread):

    def __init__(self, port, host='localhost'):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, port))
        # Create public/private key if doesn't exist

    def send_message(self, msg):
        # Encrypt chat messages in this method
        data = bytes(msg, 'utf-8')
        self.socket.send(data)

    def ReceiveMessage(self):
        # Decrypt chat messages in this method
        while(True):
            data = self.socket.recv(1024)
            if data:
                msg = data.decode('utf-8')
                print(msg)

    def run(self):
        print("Starting Client")

        # Currently only sends the username
        self.username = input("Username: ")
        data = bytes(self.username, 'utf-8')
        self.socket.send(data)

        # Need to get session passphrase
        
        # Starts thread to listen for data
        threading.Thread(target=self.ReceiveMessage).start()
        
        while(True):
            msg = input()
            self.send_message(msg)
        
if __name__ == '__main__':
    client = ChatClient(PORT)
    client.start() # This start run()
