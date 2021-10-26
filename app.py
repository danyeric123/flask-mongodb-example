from flask import Flask, render_template,request
from flask.helpers import url_for
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
import os

from werkzeug.utils import redirect

from models import Todo

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
app = Flask(__name__)

# app.config['MONGO_URI'] = DATABASE_URL
app.config['MONGODB_SETTINGS'] = {
    'db': 'flaskmongo',
    'host': DATABASE_URL
}
mongo = MongoEngine()
mongo.init_app(app)

@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'POST':
    new_todo = request.form.get('new-todo')
    Todo(content=new_todo).save()
  all_todos = Todo.objects()
  return render_template('index.html', todos=all_todos)

@app.route('/delete/<id>')
def delete_todo(id):
  Todo.objects(id=id).delete()
  return redirect(url_for('index'))

@app.route('/todos/<id>')
def show_todo(id):
  todo = Todo.objects.get(id=id)
  return render_template('show.html',todo=todo)

@app.route('/todos/<id>/edit',methods=['POST','GET'])
def update(id):
  if request.method == 'POST':
    completed = True if request.form.get("complete") else False
    Todo.objects(id=id).update(
      content=request.form.get("content"),
      complete=completed
      )
    return redirect(url_for('index'))
  todo = Todo.objects.get(id=id)
  return render_template('update.html',todo=todo) 

if __name__ == '__main__':
  app.run()