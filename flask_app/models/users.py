from flask import flask, render_template, request, redirect, session
app = flask(__name__)
app.secret_key = "therapy!!!"

@app.route('/')
def index():
    return render_template('soap_notes.html')