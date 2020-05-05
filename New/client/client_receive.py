
import socket


def get_header(s):
    d = ""
    fsize = 0
    fsize_b = ""

    fsize_b = get_data(s, 10)
    if fsize_b is not "":
        print("fsizeb: ", fsize_b, " type: ", type(fsize_b))
        fsize = int(fsize_b)

    d = get_data(s, fsize)
    return d


def get_data(s, b):

    buff = ""
    tbuff = ""

    while len(buff) < b:

        tbuff = s.recv(b)
        tbuffDec = tbuff.decode()

        if not tbuff:
            break
        buff += tbuffDec

    return buff
