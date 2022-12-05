#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'secure'

if __name__ == "__main__":
    app.run('0.0.0.0', 7002, ssl_context=('cert.pem', 'key.pem'))