from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/sleepdata'
db = SQLAlchemy(app)

class UserDataFiles(db.Model):
    __tablename__ = 'userdatafiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

def __repr__(self):
    return f' <UserDataFiles {self.id} {self.name}>'

db.create_all()

@app.route('/')
def index():
    return render_template('index.html', data= UserDataFiles.query.all() )  