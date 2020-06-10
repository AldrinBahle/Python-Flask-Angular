from flask import Flask
import mysql.connector

app = Flask(__name__)
db_connection = mysql.connector.connect(
    host="uzuri.ctqphpecp3xd.ap-south-1.rds.amazonaws.com",
    user="Mcebo",
    passwd="uzuri@0002",
  )

mysql = db_connection.cursor()
