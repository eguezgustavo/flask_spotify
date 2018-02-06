from flask import Flask
from subprocess import call

app = Flask(__name__)

@app.route('/play')
def hello_world():
    call(["spotify", "play"])
    return 'Playing..'

@app.route('/stop')
def stop():
    call(["spotify", "stop"])
    return 'stopped'

if __name__ == "__main__":
    app.run()

