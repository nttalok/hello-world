
from flask import Flask
from flask import render_template, url_for

import os
import socket


application = Flask(__name__)

@application.route("/")
def hello():
        return  render_template('index.html', name=os.getenv("NAME", "Customer"), hostname=socket.gethostname())

if __name__ == "__main__":
        application.run()

