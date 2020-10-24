from flask import Flask, render_template, request

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET'])
def index_get():
    return 'HELLO WORLD'

@app.route('/hello/<input_name>')
def name_get(input_name):
    return f'HELLO {input_name}'

@app.route('/html')
def html_get():
    return render_template('index.html', messages=messages)

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
    
app.run()
