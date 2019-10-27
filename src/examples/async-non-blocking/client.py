from async_client import AsyncClient
import event_loop
from time import sleep
from utils import write_console, flush
from datetime import datetime
import sys

client = AsyncClient()

def calculation():
    while True:
        write_console("Current time: %s" % (datetime.now()))
        yield
    

host1 = ('localhost', 1234)
host2 = ('localhost', 5678)

tasks = [
    client.get(host1), 
    calculation(), 
    client.put(host2, 'some data')
]

print("Running async client with %s tasks\n\n" % len(tasks))

for i in reversed(range(10)):
    sys.stdout.write("Starting in: %s\r" % i)
    sys.stdout.flush()
    sleep(1)

event_loop.run(*tasks)
flush()


