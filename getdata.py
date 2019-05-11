from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json


local_server=True
with open('config.json','r')as c:
    params=json.load(c)["params"]

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

@app.route("/")
def info():
    cur = db.connection.cursor()
    cur.execute("select * from contacts")
    rv = cur.fetchall()
    return jsonify(rv)

app.run(debug=True)