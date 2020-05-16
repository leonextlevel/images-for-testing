from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='home')


@app.route('/imagem')
def imagem():
    return render_template('imagem.html', title='imagem')


@app.route('/contato')
def contato():
    return render_template('contato.html', title='contato')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title='sobre')
