from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = 'woinwefoinef;oinaf'

users = []
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
FIRST_NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
LAST_NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'[0-9]')

@app.route('/')
def index():
    global users
    return render_template('index.html', users=users)

@app.route('/register', methods=['post'])
def register():
    global users
    if not request.form['email']:
        flash("Please enter your email address.", "error")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash(u"Please enter a valid email address.", "error")
    elif not request.form['first_name']:
        flash("Please enter your first name.", "error")
    elif not FIRST_NAME_REGEX.match(request.form['first_name']):
        flash("First name may only contain letters", "error")
    elif not request.form['last_name']:
        flash("Please enter your last name.", "error")
    elif not LAST_NAME_REGEX.match(request.form['last_name']):
        flash("Last name may only contain letters", "error")
    elif not request.form['password']:
        flash("Please enter a password", "error")
    elif not request.form['password_confirm']:
        flash("Please confirm your password", "error")
    elif request.form['password'] != request.form['password_confirm']:
        flash("Your password does not match", "error")
    else:
        flash("Success! Thank you for registering.")
        users = [request.form['email'], request.form['first_name'],
                request.form['last_name'], request.form['password']]
    return redirect('/')

app.run(debug=True)
