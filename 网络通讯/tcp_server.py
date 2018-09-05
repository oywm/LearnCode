from socket import *
from multiprocessing import Process, Lock
import sys


class Myserver(object):
    def __init__(self, address):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(address)
        self.server_socket.listen(5)
        self.client_socket1, self.client_address = self.server_socket.accept()
        self.recv_data = None

    def start_server(self):
        while True:
            self.recv_information()
            self.send_information()

    def recv_information(self):
        self.recv_data = str(self.client_socket1.recv(1024), encoding='utf-8')
        if self.recv_data:
            print('客户端对我说：\n%s' % self.recv_data)
        if self.recv_data == '拜拜':
            self.client_socket1.close()

    def send_information(self):
        print("输入你想对客户端说的话:")
        data = input()
        if data is None:
            self.client_socket1.send('')
        if data:
            send_data = data.encode('utf-8')
            self.client_socket1.send(send_data)


def main():
    server = Myserver(('', 6789))
    server.start_server()


if __name__ == '__main__':
    main()
