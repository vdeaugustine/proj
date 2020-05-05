
import socket


def get_header(s):
    d = ""
    fsize = 0
    fsize_b = ""
    fsize_b = get_data(s, 10)
    fsize = int(fsize_b)

    d = get_data(s, fsize)
    return d


def get_data(s, b):

    buff = ""
    tbuff = ""

    while len(buff) < b:
        tbuff = s.recv(b)

        if not tbuff:
            break
        buff += tbuff

    return buff
