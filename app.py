import os
from dotenv import load_dotenv
from flask import Flask, render_template ,redirect, url_for
import json
from flask_mysqldb import MySQL

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("APP_SECRET_KEY")
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'sample'

mysql = MySQL(app)

from sample import sample
app.register_blueprint(sample,url_prefix="/sample")

@app.route("/")
def index():
    return f"Index"

if __name__ == "__main__":
    app.run()




