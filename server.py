import sys
import argparse
import socket
import signal
#import confundo
#from confundo.socket import socket
#from confundo import socket
#from.confundo import socket
from .socket import Socket
from confundo.socket import Socket



SERVER_HOST = 'localhost'
SERVER_PORT = 8888
BUFFER_SIZE = 10000000
TIMEOUT = 10


def main():
    # Main function that sets up the server and handles incoming connections
    try:
        sock = confundo.Socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setblocking(True)
        sock.bind((SERVER_HOST, SERVER_PORT))
        sock.listen(1)
    except OSError:
        sys.stderr.write("ERROR: Could not start server\n")
        sys.exit(1)

    while True:
        try:
            conn, addr = sock.accept()
            conn.settimeout(TIMEOUT)
            # Receive the file data
            with open("received_file.txt", "wb") as f:
                while True:
                    data = conn.recv(BUFFER_SIZE)
                    print(bytes(data))
                    if not data:
                        break
                    f.write(data)
        except (ConnectionError, TimeoutError):
            sys.stderr.write("ERROR: Connection or transmission error\n")
        finally:
            conn.close()


if __name__ == '__main__':
    main()


'''
import sys
import argparse
import socket
import signal

import confundo

# for testing, replace socket.socket with confundo.Socket()
# or just use the reference server (check Piazza or consult the instructor)

# the server can only work in a single threaded mode, one client at a time (no parallel,
# neither concurrent nor threaded---simplifications in the socket implementation)

# Other than that, standard socket interface should work

def start():
    pass

if __name__ == '__main__':
    start()
'''