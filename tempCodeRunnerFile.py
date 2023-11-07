import socket
import sys
import argparse
host = 'localhost'
data_buff = 2048
backlog = 5
def TCPserver1(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(sock.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print('Starting up echo server on %s port %s server_address')
    sock.bind(server_address)
    sock.listen(backlog)
    while True:
        print("Waiting to recieve message from client")
        client, address = sock.accept()
        data = client.recv(data_buff)
        if data:
            print("Data: %s" %data)
            client.send(data)
            print("Sent %s bytes back to %s" %(data, address))
            sock.close()
        if __name__=='__main__':
            parser = argparse.ArgumentParser(description='Socket Server')
            parser.add_argument('--port', action="store", dest="port", type=int, required=True)
            given_args = parser.parse_args()
            port = given_args.port
            TCPserver1(port)