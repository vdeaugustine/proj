
from socket import *
import server_send_data as ssd
import server_receive as sr
import ephemeral as e
import sys
import server_run_commands as scmd


if __name__ == '__main__':

    numOfArguments = len(sys.argv)
    if numOfArguments == 2:
        servPort = sys.argv[1]
        if servPort.isdigit():
            print("Server port is in right format")
            servPort = int(servPort)
        else:
            print("Server port needs to be a digit")
    else:
        print("Incorrect invocation. Server should be invoked as: "
              "server.py <server port>")
        quit()

    initServSock = socket(AF_INET, SOCK_STREAM)
    initServSock.bind(('', servPort))
    initServSock.listen(1)

    print("Server open: ")
    interSock , iSockAddr = initServSock.accept()
    print("Established connection with: ", iSockAddr)

    all = ""

    while True:
        inst = sr.get_header(interSock)

        if inst.startswith("ls"):
            print("Performing ls")
            sendSocket = e.ephemeral(interSock)
            dataToSend = scmd.run_ls()
            # codedData = dataToSend.encode()
            ssd.send_it(sendSocket, dataToSend)
            print("Finished ls")
            sendSocket.close()

        if inst.startswith("quit"):
            interSock.close()
            scmd.run_quit()
            break

        if inst.startswith("put"):
            print("User entered put command.")

        if inst.startswith("get"):
            print("User entered get command.")

    interSock.close()






