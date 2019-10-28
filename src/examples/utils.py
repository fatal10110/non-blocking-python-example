import sys
import inspect
from threading import Lock

lock = Lock()
last_writer = None
writers = {}
colors = ["32", "34", "35"]

def write_console(text, name=None, end="\r"):
    lock.acquire()
    global last_writer, colors, writers

    if not name:
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        name = calframe[1][3]

    if last_writer and last_writer != name:
        sys.stdout.write("\n")

    if name not in writers:
        writers[name] = colors.pop()
    
    last_writer = name
    
    sys.stdout.write("\033[1;%s;40m %s::\033[0;37;40m" % (writers[name], last_writer))
    sys.stdout.write("%s %s" % (text, end))
    sys.stdout.flush()
    lock.release()    

def flush():
    sys.stdout.write("\n")
    sys.stdout.flush()
