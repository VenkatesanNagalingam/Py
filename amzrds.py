import os
import flask
import sys
import logging
import pymysql
app = flask.Flask(__name__)

@app.route("/")
def webh():
  
  return "Hello world"
if __name__ == '__main__':
  app.run()
