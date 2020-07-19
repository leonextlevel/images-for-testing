import os
import cv2
import zipfile
from io import BytesIO
from app import app, db
from flask import render_template, flash, redirect, url_for, send_file, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from app.forms import LoginForm, RegistrationForm, ImageForm, GenerateImageForm
from app.models import User, UserImage
from app.utils import allowed_file
from app.transform import img_rotated


@app.route('/imagem/download-zip/<int:pk>')
def download_zip(pk):
    memory_file = BytesIO()
    zf = zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_STORED)
    files = [f.image.url for f in UserImage.query.filter_by(parent=pk)]
    # import pdb; pdb.set_trace()
    for file in files:
        zf.write(file, os.path.basename(file))
    zf.close()
    memory_file.seek(0)
    return send_file(memory_file, mimetype='application/zip', as_attachment=True, attachment_filename='images.zip')


@app.route('/imagem/download/<pk>', methods=['GET'])
def download(pk):
    image = UserImage.query.get(pk).image.url
    # import pdb; pdb.set_trace()
    return send_file(image, as_attachment=True)


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
    return render_template('home.html', title='home', user=current_user)


@app.route('/imagem', methods=['GET', 'POST'])
@login_required
def imagem():
    form = ImageForm()
    if form.validate_on_submit():
        file = form.image.data
        # import pdb; pdb.set_trace()
        user_image = UserImage(user=current_user, image=file)
        db.session.add(user_image)
        db.session.commit()
        flash('Imagem base salva!')
        return redirect(url_for('imagem'))
    images = UserImage.query.filter_by(user=current_user, parent=None)
    return render_template('imagem.html', title='imagem', form=form, user=current_user, images=images)


@app.route('/imagem/<pk>', methods=['GET', 'POST'])
@login_required
def imagem_detail(pk):
    imagem = UserImage.query.get(pk)
    form = GenerateImageForm()
    if form.validate_on_submit():
        nw_image = img_rotated(imagem.image.url)
        
        # import pdb; pdb.set_trace()
        user_image = UserImage(user=current_user, image=nw_image, parent=imagem.id)
        db.session.add(user_image)
        db.session.commit()
        flash('Nova imagem gerada com sucesso!')
    filhos = UserImage.query.filter_by(parent=imagem.id)
    return render_template('imagem_detail.html', title='imagem', obj=imagem, form=form, filhos=filhos)


@app.route('/contato')
@login_required
def contato():
    return render_template('contato.html', title='contato')


@app.route('/sobre')
@login_required
def sobre():
    return render_template('sobre.html', title='sobre')
