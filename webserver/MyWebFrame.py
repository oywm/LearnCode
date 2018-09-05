# coding:'utf-8'
import time


HTML_ROOT_DIR = './html'


class Application(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get('PATH_INFO', '/')
        if path.startswith('/static'):
            file_name = path[7:]
            if '/' == file_name:
                file_name = '/index.html'
            try:
                f = open(HTML_ROOT_DIR + file_name, 'r')
            except IOError:
                status = '404 Not Found'
                headers = []
                start_response(status, headers)
                return 'not found'
            else:
                file_data = f.read()
                print(type(file_data))
                f.close()
                status = '200 OK'
                headers = []
                start_response(status, headers)

                return file_data

        path = path[:-3]
        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response)

        status = '404 Not Found'
        headers = []
        start_response(status, headers)

        return 'not found'


def show_time(env, start_response):
    status = '200 OK'
    headers = [('Server', 'My server')]
    start_response(status, headers)
    return time.ctime()


def say_hello(env, start_response):
    status = '200 OK'
    headers = []
    start_response(status, headers)
    return 'hello,程序员'


urls = [
    ('/ctime', show_time),
    ('/sayhello', say_hello)
]

app = Application(urls)
