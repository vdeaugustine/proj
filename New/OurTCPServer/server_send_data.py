
def send_it(s, d):

    # print("Data: ", d, "Type of data: ", type(d))
    d_size = str(len(d))

    # set header to 10 bytes
    while len(d_size) < 10:
        d_size = "0" + d_size

    data = d_size + d
    total = 0

    # ensure all data is sent
    while total != len(data):
        sendingThis = data[total:]
        encodeSend = sendingThis.encode()
        # print("Type of sendingThis: ", type(sendingThis))
        total += s.send(encodeSend)