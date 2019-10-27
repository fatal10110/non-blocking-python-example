import errno
import socket
from contextlib import contextmanager
from utils import write_console

BUFF_SIZE = 1024

from event_loop import Operations

class AsyncClient(object):
    def get(self, host_port):
        with self._connect(host_port) as s:
            yield from self._read(s)



    def put(self, host_port, data):
        with self._connect(host_port) as s:
            yield from self._write(s, data)

    
    @contextmanager
    def _connect(self, host_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(host_port)
            s.setblocking(0)
            
            yield s


    def _read(self, sock):
        yield Operations.READ, sock
       
        data = sock.recv(BUFF_SIZE)

        while data:
            write_console("Client received data %s" % data)
            yield Operations.READ, sock
            data = sock.recv(BUFF_SIZE)

    def _write(self, sock, to_send):
        total_sent = 0
        for _ in range(3):
            data = to_send * 1024 * 256

            while len(data):
                try:
                    sent = sock.send(data.encode())
                    total_sent += sent
                    write_console("Data sent %s" % total_sent)
                    data = data[sent:]
                except socket.error as e:
                    if e.errno != errno.EAGAIN:
                        raise e

                    yield Operations.WRITE, sock
