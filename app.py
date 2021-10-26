from flask import Flask, render_template,request
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import datetime
from bson.objectid import ObjectId
from bson import json_util
import os
import json

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
app = Flask(__name__)

app.config['MONGO_URI'] = DATABASE_URL
mongo = PyMongo(app)

todos = mongo.db.todos

@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'POST':
    new_todo = request.form.get('new-todo')
    todos.insert_one({'content' : new_todo, 'complete' : False})
  all_todos = todos.find()
  return render_template('index.html', todos=all_todos)


if __name__ == '__main__':
  app.run()