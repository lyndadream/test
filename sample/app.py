from flask import Flask, render_template, url_for, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hogehoge'

@app.route("/", methods=['POST','GET'])
def index():
   return render_template('index.html')

@app.route("/todo", methods=['GET', 'POST'])
def todo():
   if request.method == 'POST':
       todo = request.form['todo']
       if todo:#todoがない1度目はこれがないとエラーになる
           todo_list = []
           if 'todo' in session:#todoがない1度目はこれがないとエラーになる
               todo_list = session['todo']
           todo_list.append(todo)
           session['todo'] = todo_list

   return render_template('index.html')

app.run(port=8000, debug=True)
