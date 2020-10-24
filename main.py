from flask import Flask, render_template
from flask import request
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET', 'POST'])
def index_get():
    if (request.method == 'GET'):
        return render_template('index.html', messages=messages)
    else:
        messages.append({
            'message': request.form['message'],
            'name': request.form['name'],
            'time': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })
        return render_template('index.html', messages=messages)

@app.route('/static/<path:subpath>')
def static_files(subpath):
    return url_for('static', filename=subpath)
