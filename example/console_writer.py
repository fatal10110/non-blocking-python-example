import sys

last_writer = None

def write_console(name, text):
    global last_writer

    if last_writer != name:
        last_writer = name
        sys.stdout.write("\n")
        
    sys.stdout.write("%s \r" % text)
    sys.stdout.flush()

def flush():
    sys.stdout.write("\n")
    sys.stdout.flush()