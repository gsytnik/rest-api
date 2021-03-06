from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	return 'Hello, world!'

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      },
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd["id"] = random.randint(0, 999999)
      
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      resp.status_code = 201 #optionally, you can always set a response code.  
      # 200 is the default code for a normal response
      return resp
   elif request.method == 'DELETE':
      userToRemove = request.get_json()
      users['users_list'].remove(userToRemove)
      resp = jsonify(userToRemove)
      resp.status_code = 204
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp

@app.route('/users/<id>', methods = ['GET', 'POST', 'DELETE'])
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           if request.method == 'DELETE':
              resp = jsonify(success=True)
              resp.status_code = 204
           return user
      return ({})
   return users

@app.route('/users/<job>')
def get_users_by_job(job):
   if job :
   	  subdict = {'users_list' : []}
   	  for user in users['users_list']:
   	  	if user['job'] == job:
   	  		subdict['users_list'].append(user)
   	  return subdict
   	  return ({})
   return users

@app.route('/users/<name>')
def get_users_by_name(name):
   if name :
   	  subdict = {'users_list' : []}
   	  for user in users['users_list']:
   	  	if user['name'] == name:
   	  		subdict['users_list'].append(user)
   	  return subdict
   	  return ({})
   return users
