# # changed line at env/libs/click/utils.py
import webbrowser
from threading import Timer
from flask import Flask, render_template
import os
import signal

app = Flask(__name__)
def open_browser():
      webbrowser.open_new("http://127.0.0.1:2000")

@app.route('/')
def hello():
    return render_template('test.html')

@app.route('/shutdown', methods=['POST'])
def stop_server():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server shutting down...'



if __name__ == '__main__':
      Timer(1, open_browser).start()     
      app.run(port=2000)
