import subprocess
import socket
import server_send_data
import os

def run_ls():
    lsData = ""
    for line in subprocess.getstatusoutput('ls -l'):
        lsData += line
    return lsData


def run_quit():
    print("Ending program")

def run_get(name_of_file, sock):
    file = open(name_of_file, "r")
    buffer = file.read(1)
    while "" != buffer:
        server_send_data.send_it(sock, buffer)
        buffer = file.read(1)
    file.close()


def run_put(name_of_file, sock):
    # if os.path.exists(name_of_file):
    pass
