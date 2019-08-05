import sys
import traceback
from flask import Flask, jsonify

import requests

app = Flask(__name__)

@app.route('/')
def index():
  try:
    url = "http://app2:5000"
    res = requests.get(url,timeout=5.0)
    return jsonify({"app1": "{0}".format(res)})
  except Exception as e:
    return jsonify({"app1": "{0}".format(e)}), 500

if __name__ == '__main__':
  app.run()