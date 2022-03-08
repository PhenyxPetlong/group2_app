import datetime
from flask import Flask, redirect, render_template, request, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

#app.secret_key = '1234567890'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'group_2'

mysql = MySQL(app)
msg = ""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.form: #that means our reg form has been submitted. Proceed to get the supplied form data and store in variables
        userName = request.form.get("username")
        passwd = request.form.get("pwd")
        rememberMe = request.form.get("remember")
    return render_template("login.html", msg = msg)



@app.route("/signup", methods=["POST", "GET"])
def register():
    if request.form: #that means our reg form has been submitted. Proceed to get the supplied form data and store in variables
        userName = request.form.get("username")
        user_mail = request.form.get("email")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        passwd = request.form.get("pwd")
        verifyPass = request.form.get("ver_pwd")
        gender = request.form.get("gender")
        terms_condition = request.form.get("tc")
    return render_template("register.html", msg = msg)

if __name__ == "__main__":
    app.run(debug=True)
  # app.run() 