# Import Flask an submodules
from flask import Flask, redirect, request, render_template, flash, session
# Importing Regex
import re

# Importing the mysqlconnection file and MySQLConnection
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'solikndfoinwekwefolknwef'
mysql = MySQLConnector(app, 'emails')
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

@app.route('/')
def index():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    #print(emails)
    return render_template('index.html', all_emails=emails)

@app.route('/register', methods=['post'])
def register():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email address.", "error")
    else:
        flash("Thank you for registering.", "success")
        query = """INSERT INTO emails (address, created_at, updated_at) 
                   VALUES (:email, NOW(), NOW())"""
        data = {
                'email': request.form['email']
                }
        #print(emails)
        mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
