from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
import re
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'woineoinsdlknaf;lknadsf'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'users')
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    #print(users)
    return render_template('index.html', users=users)

@app.route('/register', methods=['post'])
def create():
    if not request.form['first_name']:
        flash('Please enter a first name', "error")
        return redirect('/')
    if len(request.form['first_name']) < 2:
        flash('Please enter a first name at least two characters long.', 
                "error")
        return redirect('/')
    if not request.form['last_name']:
        flash('Please enter a last name', "error")
        return redirect('/')
    if len(request.form['last_name']) < 2:
        flash('Please enter a last name at least two characters long.', "error")
        return redirect('/')
    if not request.form['email']:
        flash('Please enter an email', "error")
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email address.', "error")
        return redirect('/')
    if not request.form['password']:
        flash('Please enter a password', "error")
        return redirect('/')
    if len(request.form['password']) < 8:
        flash('Please enter at least 8 characters for the password', "error")
        return redirect('/')
    if not request.form['password_confirm']:
        flash('Please confirm your password', "error")
        return redirect('/')
    if not request.form['password'] == request.form['password_confirm']:
        flash('Your password and confirmation do not match.', "error")
        return redirect('/')
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    pw_hash = bcrypt.generate_password_hash(password)
    query = """
            INSERT INTO users(first_name, last_name, email, pw_hash, 
            created_at, updated_at)
            VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())
            """
    data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email, 
            'pw_hash': pw_hash
            }
    mysql.query_db(query, data)
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    user = mysql.query_db(query, data)
    session['user_id'] = user[0]['id']
    return render_template('success.html', user=user[0])

@app.route('/login', methods=['post'])
def login():
    print('in!')
    if not request.form['email']:
        flash('Please enter an email address.', 'error')
        return redirect('/')
    if not request.form['password']:
        flash('Please enter a password.', 'error')
        return redirect('/')
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {
            'email': email, 
            }
    user = mysql.query_db(query, data)
    #print(user[0]['email'])
    #print(user[0]['pw_hash'])
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        session['user_id'] = user[0]['id']
        #print(session['user_id'])
        return render_template('success.html', user=user[0])
    else:
        flash("Password incorrect", "error")
        return redirect('/')

app.run(debug=True)
