from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_mysqldb import MySQL
import os,json,math


local_server = True

app = Flask(__name__)

app.secret_key = "Secret_kety"


if(local_server):
	app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@127.0.0.1/Iste"
else:
	app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@127.0.0.1/Iste"


db = SQLAlchemy(app)



class Contact(db.Model):
	S_no = db.Column(db.Integer, primary_key=True)
	First_name = db.Column(db.String(80), primary_key=False, nullable=False)
	Last_name = db.Column(db.String(80), primary_key=False, nullable=False)
	Email = db.Column(db.String(20), nullable=False)
	Phone = db.Column(db.Integer, primary_key=False, nullable=False)
	Address = db.Column(db.String(80), primary_key=False, nullable=False)
	Message = db.Column(db.String(120), primary_key=False, nullable=False)
	Date = db.Column(db.String(12),primary_key=False,nullable=True)



@app.route("/contact", methods = ["GET","POST"])
def contact():
	if(request.method=="POST"):
		first_name=request.form.get("first_name")
		last_name=request.form.get("last_name")
		email=request.form.get("email")
		phone=request.form.get("phone")
		address=request.form.get("address")
		message=request.form.get("message")
		

		entry = Contact(First_name = first_name,Last_name=last_name,Phone=phone,Email = email,Address=address,Message = message,Date=datetime.now())
		
		db.session.add(entry)
		db.session.commit()
		return render_template("index.html", value=True)
	return render_template("index.html")



app.run(debug=True, port=8001)