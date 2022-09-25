import sys
import socket

from . import helper


def read_file(filename):
    # with open(filename, 'r') as fh:
    #     content = fh.read()
    # return content
    fh = open(filename, 'r')
    return fh.read()


def tcp_out():
    HOST = '127.0.0.1'
    PORT = 8888

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"Hello, world")
        # data = s.recv(1024)
        # print(f"Received {data!r}")


def tcp_in():
    HOST = '127.0.0.1'
    PORT = 8888

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            # print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


def udp_out():
    UDP_IP = '127.0.0.1'
    UDP_PORT = 8888
    MESSAGE = b'Hello, World!'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


def udp_in():
    UDP_IP = '127.0.0.1'
    UDP_PORT = 8888

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        # print("received message: %s" % data)
