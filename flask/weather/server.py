from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "weaterappleinsoinwoineoindfljsdoijsdfoij"


@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
