from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db= SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    with app.app_context():
        db.create_all()

@app.route('/')
def formulario():
    return render_template('formulario.html')



@app.route('/adicionar',methods=['POST'])
def adicionar():
    if request.method == 'POST':
        email= request.form['email']
        senha= request.form['senha']


        novo_usuario = Usuario = Usuario(email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commmit()