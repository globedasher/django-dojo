from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
import re
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'soinwionwef90hj123'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'users')
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', users=users)


@app.route('/register', methods=['post'])
def create():
    if not request.form['first_name']:
        flash("Please enter your first name", "error")
        return redirect('/')
    elif len(request.form['first_name']) < 2:
        flash("Please enter at least two characters for your first name.", "error")
        return redirect('/')
    if not request.form['last_name']:
        flash("Please enter your last name", "error")
        return redirect('/')
    elif len(request.form['last_name']) < 2:
        flash("Please enter at least two characters for your last name.", "error")
        return redirect('/')
    if not request.form['email']:
        flash("Please enter an email address", "error")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email address", "error")
        return redirect('/')
    if not request.form['password']: 
        flash("Plese enter your password.", "error")
        return redirect('/')
    elif not request.form['password_confirm']:
        flash("Please confirm your password", "error")
        return redirect('/')
    elif len(request.form['password']) < 8:
        flash("Please enter a password longer than eight characters.", "error")
        return redirect('/')
    elif request.form['password'] == request.form['password_confirm']:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        query = """
                INSERT INTO users (first_name, last_name, email, pw_hash,
                created_at, updated_at)
                VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())
                """
        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'pw_hash':pw_hash
                }
        mysql.query_db(query, data)
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user = mysql.query_db(query, data)
        flash('Registration Successful. Hello,')
        # RM- I understand I could perform a query on each route and pass the
        # values back on the route, but I would hate to use up server time each
        # time I wanted to identify the user name. Therefore, I shall hold the
        # user information in session.
        session['user_id'] = user[0]['id']
        session['first_name'] = user[0]['first_name']
        session['email'] = user[0]['email']
        return redirect('/wall')


@app.route('/login', methods=['post'])
def verify():
    if not request.form['email']:
        flash("Please enter an email address.", "error")
        return redirect('/')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email address.", "error")
        return redirect('/')
    if not request.form['password']:
        flash("Please enter your password.", "error")
        return redirect('/')
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = { 'email': request.form['email'] }
    user = mysql.query_db(query, data)
    if not bcrypt.check_password_hash(user[0]['pw_hash'],
            request.form['password']):
        flash("Password incorrect", "error")
        return redirect('/')
    if bcrypt.check_password_hash(user[0]['pw_hash'], request.form['password']):
        flash('Login Successful. Hello,')
        # RM- I understand I could perform a query on each route and pass the
        # values back on the route, but I would hate to use up server time each
        # time I wanted to identify the user name. Therefore, I shall hold the
        # user information in session.
        session['user_id'] = user[0]['id']
        session['first_name'] = user[0]['first_name']
        return redirect('/wall')


@app.route('/wall')
def wall():
    wall_query = """SELECT *, messages.id AS id, messages.created_at AS time,
    users.first_name AS poster
                     FROM messages 
                     JOIN users 
                     ON users.id = messages.user_id
                     ORDER BY messages.id DESC
                     """
    comment_query = """SELECT * FROM comments
                       JOIN users
                       ON comments.user_id = users.id
                       """
    data = mysql.query_db(wall_query)
    comment_data = mysql.query_db(comment_query)
    #print(data[0])
    #print(comment_data)
    return render_template('wall.html', data=data, comment_data=comment_data)


@app.route('/message', methods=['post'])
def message():
    wall_post = """INSERT INTO messages(message, created_at, updated_at, user_id)
                VALUES (:message, NOW(), NOW(), :user_id)
                """
    post_data = {
            'message': request.form['message'],
            'user_id': session['user_id']
            }
    print(post_data)
    mysql.query_db(wall_post, post_data)
    return redirect('/wall')


@app.route('/comment', methods=['post'])
def comment():
    comment_post = """INSERT INTO comments(comment, created_at, updated_at,
                   user_id, message_id)
                   VALUES (:comment, NOW(), NOW(), :user_id, :message_id)
                   """
    print(request.form['hidden_id'])
    post_data = {
            'comment': request.form['comment'],
            'message_id': request.form['hidden_id'],
            'user_id': session['user_id']
            }
    mysql.query_db(comment_post, post_data)
    return redirect('/wall')


@app.route('/logoff')
def logoff():
    session['user_id'] = ""
    session['first_name'] = ""
    return redirect('/')

app.run(debug=True)
