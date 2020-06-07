import os
from app import app, db
from flask import render_template, flash, redirect, url_for, send_file, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils import secure_filename
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app.utils import allowed_file


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuário ou Senha inválido')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Parabéns, usuário cadastrado!')
        return redirect(url_for('login'))
    return render_template('registro.html', title='registro', form=form)


@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template('home.html', title='home')


@app.route('/imagem', methods=['GET', 'POST'])
@login_required
def imagem():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Sem arquivo!')
            return redirect(request.url)
        file = request.files['file']
        if not file.filename:
            flash('Adicione uma imagem válida')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Imagem salva!')
            return redirect(url_for('home'))
        else:
            flash('Arquivo inválido. Verifique se é uma imagem no formatos .png, .jpg ou .jpeg')
    return render_template('imagem.html', title='imagem')


@app.route('/contato')
@login_required
def contato():
    return render_template('contato.html', title='contato')


@app.route('/sobre')
@login_required
def sobre():
    return render_template('sobre.html', title='sobre')
