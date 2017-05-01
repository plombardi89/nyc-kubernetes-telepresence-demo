#!/usr/bin/env python

import os
import time

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return jsonify(message="Hello NYC! This service is running on my local PC! WAHOO!".format(name),
                   time=int(round(time.time() * 1000)))


@app.route('/health', methods=['GET', 'HEAD'])
def health():
    return '', 200


def main():
    app.run(debug=True, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
