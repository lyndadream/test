from flask import Flask, render_template, url_for, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hogehoge'

@app.route("/", methods=['POST', 'GET'])
def index():
   return render_template('index.html')

@app.route("/soft", methods=['POST', 'GET'])
def soft():
    want_list = []
    want = request.form['want']
    want_list.append(want)
    session['spec'] = want_list
    return render_template('index.html')

app.run(port=8000, debug=True)
