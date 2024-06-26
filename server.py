import os
import sqlite3

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template("base.html")
    elif request.method == 'POST':
        database = sqlite3.connect("base.sqlite")
        database.cursor().execute(f"INSERT INTO email(email) VALUES('{request.form['phonenumber']}')")
        database.commit()
        return "Форма отправлена"

@app.route('/database')
def database():
    database = sqlite3.connect("base.sqlite")
    numbers = database.cursor().execute(f"SELECT email FROM email")
    return render_template("table.html", numbers=numbers)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
