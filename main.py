from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
app = Flask(__name__)
db = SQLAlchemy(app)
class security_test(db.Model):
    __tablename__ = 'security_test'
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(30), unique=True, nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)


    def __init__(self, name):
        self.name = name
# #####################
@app.route("/submit", methods=['POST'])
def submit():
    data = request.values['data']
    print(data)
    new_sec = security_test(data)
    db.session.add(new_sec)
    db.session.commit()
    return render_template('input.html',**locals())
@app.route('/')
def index():
    # Create data
    basedir = os.path.abspath(os.path.dirname(__file__))
    # app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
    db.create_all()
    return render_template("input.html")
app.run(debug=True)
# #####################
# @app.route("/")
# def index():
#     return render_template("input.html")
# app.run()