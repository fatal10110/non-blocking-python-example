import socket
import errno
import sys
from time import sleep

PORT = 1234 if len(sys.argv) == 1 else int(sys.argv[1])
HOST = 'localhost'

IS_READ = sys.argv and len(sys.argv) > 2
BUFF_SIZE = 1024 * 15

print("Starting server for %s on %s:%s \n\n" % ("read" if IS_READ else "write", HOST, PORT))

for i in reversed(range(10)):
    sys.stdout.write("Starting in: %s\r" % i)
    sys.stdout.flush()
    sleep(1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    
    with conn:
        print('Connected by', addr)

        if IS_READ:
            print("Checking socket for available data")

            data = conn.recv(BUFF_SIZE)
            chunks = 1

            while data:
                sys.stdout.write("Received data size %s from chunk %s \r" % (len(data), chunks))
                sys.stdout.flush()
                data = conn.recv(BUFF_SIZE)
                chunks += 1
                sleep(0.2)

            print("\n\n Buffer socket read finished!!! \n\n")
        else:
            for i in range(5):
                try:
                    print("Sending %s\r" % ('some_data %s' % i,))
                    conn.send(('some_data %s' % i).encode())
                    sleep(7)
                except socket.error as e:
                    if e.errno != errno.EAGAIN:
                        raise e

                    sleep(7)