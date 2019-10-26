from async_client import AsyncClient
import event_loop
from time import sleep
from console_writer import write_console, flush

client = AsyncClient()

def cpu_func():
    i = 0

    while True:
        sleep(0.2)
        i += 1
    
        write_console("cpu_func", "Counted to %s" % i)
        
        yield

host1 = ('localhost', 1234)
host2 = ('localhost', 5678)

event_loop.run(client.get(host1), cpu_func(), client.put(host2, 'some data')    )
flush()


