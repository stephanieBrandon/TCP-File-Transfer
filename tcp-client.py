import socket
import sys
import argparse
host = 'localhost'
def TCPClient1(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print("Connecting to %s port %s" %server_address)
    sock.connect(server_address)
    try:
        message = "Test message. This will be echoed"
        print('Sending "%s"' %message)
        sock.sendall(message.encode('utf-8'))
        amount_recieved = 0
        amount_expected = len(message)
        while amount_recieved < amount_expected:
            data = sock.recv(16)
            amount_recieved += len(data)
            print("Recieved: %s" %data)
    except socket.error as e:
        print("Socket error: %s"%str(e))
    except Exception as e:
        print("Other exception: %s" %str(e))
    finally:
        print("Closing connection to the server")
        sock.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    TCPClient1(port)