from flask import Flask, render_template, request, redirect, session, flash, jsonify

app = Flask(__name__)
app.secret_key = "woinwoinweoinwef"
from mysqlconnection import MySQLConnector
"""
Set variable 'mysql' to be an instance of the MySQLConnector class taking our
entire app as the first argument and the database name as the second argument.
"""
mysql = MySQLConnector(app, 'myownapi')


@app.route('/quotes')
def index():
    query = "SELECT * FROM quotes"
    quotes = mysql.query_db(query)
    return render_template ('index.html', quotes=quotes)

@app.route('/quotes/index_json')
def index_json():
    query = "SELECT * FROM quotes"
    quotes = mysql.query_db(query)
    return jsonify(quotes=quotes)

@app.route('/quotes/index_html')
def index_partial():
    query = "SELECT * FROM quotes"
    quotes = mysql.query_db(query)
    return render_template('partials/quotes.html', quotes=quotes)

@app.route('/quotes/create', methods=['post'])
def create():
    quote = request.form
    query = """INSERT INTO quotes(author, quote)
            VALUES ('{}', '{}')""".format(quote['author'], quote['quote'])
    mysql.query_db(query)
    return_query = "SELECT * FROM quotes"
    quotes = mysql.query_db(return_query)
    return render_template('partials/quotes.html', quotes=quotes)

app.run(debug=True)
