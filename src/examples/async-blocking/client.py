import asyncio
from utils import write_console, flush

import requests

async def request(name):
    write_console("Requesting...", name, end='\n')
    response = requests.get('http://localhost:5000/')
    
    write_console("Got response for %s:%s" % (name, response), name, end='\n')

async def main():
    await asyncio.gather(request("First"), request("Second"), request("Third"))
    flush()

print("Running async with blocking IO \n")
print("-" * 10)

asyncio.run(main())
