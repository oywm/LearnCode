from socket import *
from multiprocessing import Process, Lock
import sys


class Client(object):
    def __init__(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.set_address = ('10.21.103.4', 6789)
        self.client_socket.connect(self.set_address)
        self.send_data = None
        self.recv_data = None

    def start_client(self):
        while True:
            self.send_information()
            self.recv_information()

    def send_information(self):
        print('请出入你想要对服务器说到话:')
        self.send_data = input().encode('utf-8')
        if self.send_data is None:
            self.client_socket.send('')
        if self.send_data:
            self.client_socket.send(self.send_data)

    def recv_information(self):

        self.recv_data = str(self.client_socket.recv(1024), encoding='utf-8')
        if self.send_data == '拜拜':
            self.client_socket.close()
        elif self.recv_data:
            print('服务器对我说:%s' % self.recv_data)
        else:
            pass


def main():
    client = Client()
    client.start_client()


if __name__ == '__main__':
    main()
