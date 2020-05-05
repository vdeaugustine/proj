import socket


def send_it(s, d):

    # print("Data: ", d, "Type of data: ", type(d))
    d_size = str(len(d))

    while len(d_size) < 10:
        d_size = "0" + d_size

    data = d_size + d
    total = 0

    while total != len(data):
        sendingThis = data[total:]
        # Have to encode it as byte type so that it can send
        bver = sendingThis.encode()
        print("bver is :", type(bver))
        total += s.send(bver)
