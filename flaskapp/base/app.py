import sqlite3
from flask import Flask, render_template, g

app = Flask(__name__)
DATABASE = "./local.db"
app.secret_key = "{SECRET_KEY}"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/db_status')
def db_connect():
    try:
        cur = get_db().cursor()
        cur.close()
        return "[DB] OK" 
    except Exception as e:
        return "[DB] Error, " + str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

