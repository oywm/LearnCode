from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
set_address = ('10.22.27.38', 6789)
client_socket.connect(set_address)
while True:
    send_data = input('请出入你想要对服务器说到话:').encode('utf-8')
    client_socket.send(send_data)
    recv_data = str(client_socket.recv(2048), encoding='utf-8')
    print('服务器对我说:\n%s' % recv_data)
    if recv_data == '拜拜':
        client_socket.close()
        break
