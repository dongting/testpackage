import sys
import socket

from . import helper


def read_file(filename):
    # with open(filename, 'r') as fh:
    #     content = fh.read()
    # return content
    fh = open(filename, 'r')
    return fh.read()


def resolve_dns(hostname):
    return socket.gethostbyname(hostname)


def tcp_out(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'GET / HTTP/1.1')
        # data = s.recv(1024)
        # print(f'Received {data!r}')


def tcp_in(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            # print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


def udp_out(host, port):
    MESSAGE = b'test'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (host, port))


def udp_in(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    while True:
        data, addr = sock.recvfrom(1024)
        # print('received message: %s' % data)
