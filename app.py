from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/sleepdata'
db = SQLAlchemy(app)

# This model or class corresponds to the userdatafiles table in the sleepdata db in postgres
class UserDataFiles(db.Model):
    __tablename__ = 'userdatafiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    fileLocation = db.Column(db.String(), nullable=False)

def __repr__(self):
    return f' <UserDataFiles {self.id} {self.name}>'

db.create_all()

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...' 



@app.route('/')
def index():
    return render_template('index.html', data= UserDataFiles.query.all() )  

