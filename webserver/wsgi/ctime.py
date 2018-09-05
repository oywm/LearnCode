import time


def application(env, start_response):
    env = {
        'Context': 'text/plain'
    }
    status = '200 OK'
    headers = [('Server', 'My server')]
    start_response(status, headers)
    return time.ctime()
