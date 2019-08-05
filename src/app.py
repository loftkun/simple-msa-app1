import sys
import traceback
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
  try:
    # get param
    interval = request.args.get('sleep')
    if interval == None:
      interval = 0
    
    # req to app2
    url = "http://app2:5000?sleep={0}".format(interval)
    res = requests.get(url,timeout=5.0)
    return jsonify({"app1": "{0}".format(res)})
  except Exception as e:
    return jsonify({"app1": "{0}".format(e)}), 500

if __name__ == '__main__':
  app.run()