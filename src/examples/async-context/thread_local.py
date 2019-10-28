from threading import local
from utils import write_console

import asyncio

th = local()

def _get_org_id():
    return th.org_id

def _set_org_id(org_id):
    th.org_id = org_id

async def write_data(data, name):
    write_console("Processing data with org id %s" % _get_org_id(), name, end="\n")
    await asyncio.sleep(2)
    write_console("Writing data to DB with org id %s" % _get_org_id(), name, end="\n")


async def run(name, org_id, data):
    _set_org_id(org_id)
    await write_data(data, name)

async def main():
    tasks = [
        run("Microsoft", "123", {'user': 'test', 'pass': "pass1"}),
        run("IBM", "456", {'user': 'test1', 'pass': "pass2"}),
        run("Facebook", "789", {'user': 'test2', 'pass': "pass3"})
    ]

    await asyncio.gather(*tasks)

print("Running async tasks with thread local")
print("-" * 10)

asyncio.run(main())