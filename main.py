from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return ("Uzuri Africa")

if __name__ == '__main__':
    app.run(debug=True)
