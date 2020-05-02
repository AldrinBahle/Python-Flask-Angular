from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''

mysql = MySQL(app)
