import select

class Operations(object):
    READ = 1
    WRITE = 2


class EventLoop(object):
    def __init__(self):
        self._descriptors = {
            Operations.READ: {},
            Operations.WRITE: {},
        }

    @property
    def readers(self):
        return self._descriptors[Operations.READ]
    
    @property
    def writers(self):
        return self._descriptors[Operations.WRITE]

    def _add_descriptor(self, operation, descriptor, task):
        self._descriptors[operation][descriptor] = task
    
    def execute(self, tasks):
        new_tasks = []

        for task in tasks:
            try:
                resp = next(task)
                
                if resp is None:
                    # non-io task
                    new_tasks.append(task)
                    continue

                operation, descriptor = resp
                self._add_descriptor(operation, descriptor, task)

            except StopIteration:
                # function completed
                pass
        
        return new_tasks + self._check_readiness()

    def _check_readiness(self):
        executable_tasks = []

        write_descriptors, read_descriptors = self.writers.keys(), self.readers.keys()

        if write_descriptors or read_descriptors:
            readable, writeable, exceptional = select.select(read_descriptors, write_descriptors, [], 0)
        
            for readable_sock in readable:
                executable_tasks.append(self.readers.pop(readable_sock))

            for writeable_sock in writeable:
                executable_tasks.append(self.writers.pop(writeable_sock))
        
        return executable_tasks

    def run(self, tasks):
        while len(tasks) or self.writers or self.readers:
            tasks = loop.execute(tasks)


loop = None

def run(*tasks):
    global loop

    if not loop:
        loop = EventLoop()

    loop.run(tasks)
        

