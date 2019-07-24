import hashlib
from flask import Flask, render_template, request, session
from database import db_session 
from models import User
from utils import get_hash

app = Flask(__name__)
app.secret_key = "{SECRET_KEY}"

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        username = request.form['username']
        password = get_hash(request.form['password'], app.secret_key)
        if User.query.filter(User.name == username).first():
            return render_template('error.html')

        u = User(username, password)
        db_session.add(u)
        db_session.commit()
        return render_template('login.html')

    return render_template('sign.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = get_hash(request.form['password'], app.secret_key)
        if User.query.filter(User.name == username and User.password == password).first():
            session['logged_in'] = True
            session['username'] = username
            return render_template('index.html')
        else:
            return "Fail"

    return render_template('login.html')    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

