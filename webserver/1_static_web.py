from socket import *
from multiprocessing import Process
import re
import sys

WSGI_ROOT_DIR = './wsgi'
HTML_ROOT_DIR = './html'


class Myserver(object):
    def __init__(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(('', 6789))
        self.response_headers = None

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
        if file_name.endswith('.py'):
            file = file_name[1:-3]
            try:
                m = __import__(file)
            except Exception:
                self.response_headers = 'HTTP/1.1 404 Not Found\r\n'
                response_body = 'NOT FOUND'
            else:
                env = {

                }
                response_body = m.application(env, self.start_response)
            response = self.response_headers + '\r\n' + response_body
        else:
            if '/' == file_name:
                file_name = '/index.html'
            try:
                f = open(HTML_ROOT_DIR + file_name, 'rb')
            except IOError:
                response_start_line = 'HTTP/1.1 404 Not Found\r\n'
                response_headers = 'Server: My server\r\n'
                response_body = 'File is not found!'
            else:
                file_data = f.read()
                f.close()

                # 构造响应数据
                response_start_line = 'HTTP/1.1 200 OK\r\n'
                response_headers = 'Server:My server\r\n'
                response_body = file_data.decode('utf-8')

            # 返回客户端的数据
                response = response_start_line + response_headers + '\r\n' + response_body
        item.send(bytes(response, 'utf-8'))
        item.close()


def main():
    sys.path.insert(1, WSGI_ROOT_DIR)
    server = Myserver()
    server.start()


if __name__ == '__main__':
    main()
