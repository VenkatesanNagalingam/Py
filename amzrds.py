import os
import flask
import sys
import logging
import pymysql
app = flask.Flask(__name__)

@app.route("/")
def webh():
  db_username = "root"
  db_password = "root1234"
  db_name = "airindiadb"
  db_endpoint = "airindiapnr.ckbmv5szbwip.us-east-1.rds.amazonaws.com"
  host=db_endpoint
  conn = pymysql.connect(host,db_username,db_password, db_name)
  print(conn)
  cur=conn.cursor()
  sql = "select * from tbl_pnr where pnr_number=54321;"
  data=cur.execute(sql)
  d=cur.fetchone()
  return d
if __name__ == '__main__':
  app.run()
