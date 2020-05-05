from socket import *
import client_send_data as csd
import client_receive as cr
import sys

if __name__ == '__main__':

    numOfArguments = len(sys.argv)
    if numOfArguments == 3:
        servPort = sys.argv[2]
        if servPort.isdigit():
            print("Server port is in right format")
            servPort = int(servPort)
        else:
            print("Server port needs to be a digit")
    else:
        print("Incorrect invocation. Client should be invoked as: "
              "client.py <server machine> <server port>")
        quit()

    servName = sys.argv[1]
    initCliSock = socket(AF_INET, SOCK_STREAM)
    initCliSock.connect((servName, servPort))

    userInput = input("ftp>")

    # ls operation
    if userInput.startswith("ls"):
        csd.send_it(initCliSock, "ls")
        ePort = int(cr.get_header(initCliSock))
        eSock = socket(AF_INET, SOCK_STREAM)
        eSock.connect((servName, ePort))
        buff = ""
        while True:
            buff = cr.get_header(eSock)
            if not buff:
                break
            print(buff)
        eSock.close()

    if userInput.startswith("put"):
        print("User entered the 'put' command")

    if userInput.startswith("get"):
        print("User entered to 'get' command.")

    initCliSock.close()
