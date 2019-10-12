import socket
import errno
import sys
from time import sleep

PORT = 1234 if len(sys.argv) == 1 else int(sys.argv[1])
HOST = 'localhost'

IS_READ = sys.argv and len(sys.argv) > 2
BUFF_SIZE = 1024 * 2


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    
    with conn:
        print('Connected by', addr)
        
        sys.stdout.write("\n")
        i = 0
        while True: 
            if IS_READ:
                data = conn.recv(BUFF_SIZE)

                while data:
                    sys.stdout.write("Received data size %s \r" % len(data))
                    sys.stdout.flush()
                    data = conn.recv(BUFF_SIZE)
            else:
                i += 1
                try:
                    conn.send(('some_data %s' % i).encode())
                    sleep(7)
                except socket.error as e:
                    if e.errno != errno.EAGAIN:
                        raise e

                    sleep(7)