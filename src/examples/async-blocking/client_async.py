import asyncio
from utils import write_console, flush

import aiohttp

async def request(name):
    write_console("Requesting...", name, end='\n')
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:5000/') as resp:
            write_console("Got response for %s:%s" % (name, await resp.text()), name, end='\n')

async def main():
    await asyncio.gather(request("First"), request("Second"), request("Third"))
    flush()

print("Running async with non-blocking IO \n")
print("-" * 10)

asyncio.run(main())
