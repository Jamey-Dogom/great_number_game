from flask import Flask, session, render_template, request, redirect
import os
import random

app = Flask(__name__)
# session needs a secret key to store your files
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    if not session.get('count'):
        session['count'] = 0
    result = 0
    if not session.get('guess'):
        rand_int = random.randint(1, 100)
        session['guess'] = str(rand_int)
    return render_template("index.html", answer = result)

@app.route('/game', methods = ["POST"])
def game():
    user_guess = request.form['guessing']
    if(int(session['guess']) > int(user_guess)):
        result = 1
    if(int(session['guess']) < int(user_guess)):
        result = 2
    if(int(session['guess']) == int(user_guess)):
        result = 3
    session['count'] += 1
    return render_template("index.html", answer = result)

if __name__ == '__main__':
    app.run(debug=True)

app.run(debug=True)