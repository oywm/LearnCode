# -*- coding=utf-8 -*-
from socket import *
from multiprocessing import Process
import re
import sys


WSGI_ROOT_DIR = './wsgi'
HTML_ROOT_DIR = './html'


class Myserver(object):
    def __init__(self, application):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(('', 6789))
        self.response_headers = None
        self.app = application

    def start(self):
        self.server_socket.listen(128)
        while True:
            cli_socket, cli_addre = self.server_socket.accept()
            print("(%s,%s)用户连接上了" % (cli_addre[0], cli_addre[1]))
            p = Process(target=self.handle_client, args=(cli_socket,))
            p.start()
            cli_socket.close()

    def start_response(self, status, headers):
        server_headers = 'HTTP/1.1 ' + status + '\r\n'
        for header in headers:
            server_headers += '%s:%s\r\n' % header
        self.response_headers = server_headers

    def handle_client(self, item):
        # 接收客户端的数据
        cli_data = item.recv(1024)
        data = cli_data.splitlines()[0].decode('utf-8')
        file_name = (re.match(r'\w+\s+(/[^ ]*) ', str(data))).group(1)
        env = {
            'PATH_INFO': file_name
        }
        response_body = self.app(env, self.start_response)
        response = self.response_headers + '\r\n' + response_body
        item.send(bytes(response, 'GBK'))
        item.close()


def main():
    sys.path.insert(1, WSGI_ROOT_DIR)
    module_name, app_name = sys.argv[1].split(':')
    m = __import__(module_name)
    app = getattr(m, app_name)
    server = Myserver(app)
    server.start()


if __name__ == '__main__':
    main()
