from flask import Flask
app = Flask(__name__)
from time import sleep


@app.route('/')
def hello_world():
    import random
    sleep(random.randint(3, 7))
    return 'Hello, World!'

if __name__ == '__main__':
        app.run(host= '0.0.0.0')
