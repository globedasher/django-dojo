"""
This is my Flask server.py file.
"""
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import os, binascii
import md5

app = Flask(__name__)
mysql = MySQLConnector(app,'users')

@app.route('/')
def index():
    query = """SELECT * FROM users ORDER BY created_at DESC"""
    users = mysql.query_db(query)
    print(users)
    return render_template('index.html', all_users=users)


@app.route('/users', methods=['POST'])
def create():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    salt = binascii.b2a_hex(os.urandom(15))
    pw_hash = md5.new(password + salt).hexdigest()
    query = """INSERT INTO users (username, email, pw_hash, 
                created_at, updated_at)
                VALUES (:username, :email, :pw_hash, NOW(), NOW())"""
    data = {
            'username': username,
            'email': email,
            'pw_hash': pw_hash
            }
    # add a user to the database!
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/login', methods=['post'])
def enter():
    pw_hash = md5.new(request.form['password']).hexdigest()
    email = request.form['email']
    query = """SELECT * FROM users 
               WHERE users.email = :email 
               AND users.pw_hash = :pw_hash"""
    data = {
            'email': email,
            'pw_hash': pw_hash
            }
    user = mysql.query_db(query, data)
    print(user)
    if not user[0]:
        flash("Invalid email address", "error")
        return redirect('/')
    if user[0]:
        if pw_hash == user[0]['pw_hash']:
            #print('YES')
            return render_template('loggedin.html')
        else:
            flash("Invalid password", "error")
            return redirect('/')

@app.route('/users/<user_id>/edit')
def edit(user_id):
    query = """SELECT * FROM users WHERE id = :id"""
    data = { 'id': user_id}
    print(data)
    users = mysql.query_db(query, data)
    print(users)
    return render_template('user.html', user=users[0])

@app.route('/users/<user_id>/update', methods=['POST'])
def update(user_id):
    query = """UPDATE users
               SET username = :username, email = :email,
                   pw_hash = :pw_hash, updated_at = NOW()
               WHERE id = :id"""
    data = {
            'username': request.form['username'],
            'email': request.form['email'],
            'pw_hash': request.form['password'],
            'id': user_id
            }
    # add a user to the database!
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/users/<user_id>/delete', methods=['POST'])
def destroy(user_id):
    query = """DELETE FROM users WHERE id = :id"""
    data = {'id': user_id}
    # add a user to the database!
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
