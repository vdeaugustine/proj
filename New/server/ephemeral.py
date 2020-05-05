from socket import *
import server_send_data as s


def ephemeral(con):

    eph = socket(AF_INET, SOCK_STREAM)
    eph.bind(('', 0))
    n = str(eph.getsockname()[1])
    s.send_it(con, n)
    eph.listen(1)

    r_sock, address = eph.accept()
    return r_sock
