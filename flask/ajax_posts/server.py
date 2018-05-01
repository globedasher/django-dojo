from flask import Flask, request, render_template, redirect, jsonify
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'soindionwef;klnwe;kn'
mysql = MySQLConnector(app, 'notes')

@app.route('/')
def index():
    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)
    return render_template('index.html', notes=notes)

@app.route('/note/json_index')
def json_index():
    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)
    return jsonify(notes=notes)

@app.route('/note/html_index')
def html_index():
    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)
    return render_template('partials/notes.html', notes=notes)


@app.route('/note/create', methods=['post'])
def create():
    #print(request.form)
    insert_query = """
            INSERT INTO notes (title, content, created_at, updated_at)
            VALUES (:title, :note, NOW(), NOW())
            """
    insert_data = {
            'title': request.form['title'],
            'note': request.form['note']
            }
    mysql.query_db(insert_query, insert_data)
    return_query = "SELECT * FROM notes"
    notes = mysql.query_db(return_query)
    return render_template('partials/notes.html', notes=notes)

# Full AJAX CRUD is working, but I didn't make the exising note update feature
# asked for in the assignment as I ran out of time.
@app.route('/note/update', methods=['GET'])
def update_form():
    update_query = "SELECT * FROM notes WHERE id = :id"
    update_data = { 'id': request.form['id']}
    notes = mysql.query_db(update_query, update_data)
    return render_template('partials/update.html', notes=notes)

@app.route('/note/update', methods=['post'])
def update():
    #print(request.form)
    update_query = """
                   UPDATE notes
                   SET title=:title, content=:note, updated_at=NOW()
                   WHERE id = :id
                   """
    update_data = {
            'id': request.form['id'],
            'title': request.form['title'],
            'note': request.form['note']
            }
    mysql.query_db(update_query, update_data)
    refresh_query = "SELECT * FROM notes"
    notes = mysql.query_db(refresh_query)
    return render_template('partials/notes.html', notes=notes)

@app.route('/note/delete', methods=['post'])
def delete():
    #print(request.form)
    delete_query = "DELETE FROM notes WHERE id = :id"
    delete_data = {'id': request.form['id']}
    mysql.query_db(delete_query, delete_data)
    refresh_query = "SELECT * FROM notes"
    notes = mysql.query_db(refresh_query)
    return render_template('partials/notes.html', notes=notes)

app.run(debug=True)
