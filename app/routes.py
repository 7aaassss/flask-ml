import os
import time

from flask import request, flash, render_template, jsonify, url_for, redirect
from werkzeug.utils import secure_filename
from app.forms import ImageForm
from app.models import images
from app import db, app
from sqlalchemy import text
from app import ml


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ImageForm()
    return render_template("index.html", form=form)


@app.route('/uploads', methods=['POST', 'GET'])
def upload_pic():
    form = ImageForm()
    if form.validate_on_submit():
        if 'file' not in request.files:
            flash('Файл не был выбран!', 'error')
            return jsonify({'status': 'error', 'message': 'Файл не был выбран!'})

        file = request.files['file']

        if file.filename == '':
            flash('Имя файла не указано!', 'error')
            return jsonify({'status': 'error', 'message': 'Имя файла не указано!'})

        if file and allowed_file(file.filename):
            count = db.session.execute(text("SELECT COUNT(*) FROM images")).fetchone()[0]


            filename = f"{count + 1}_{secure_filename(file.filename)}"


            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)


            file.save(filepath)

            uploaded_file = images(filename=filename)


            db.session.add(uploaded_file)


            db.session.commit()

            selected_method = request.form['methodSelect']
            if selected_method == 'DETR':
                obr = ml.show_detected_image(filepath, 'd')
            elif selected_method == 'YOLO':
                obr = ml.show_detected_image(filepath, 'y')

            flash('GOOd', 'success')
            return render_template('image.html', filename=obr)

        flash('Недопустимый тип файла!', 'error')
        return jsonify({'status': 'error', 'message': 'Недопустимый тип файла!'})

    flash('Ошибка валидации формы!', 'error')
    return jsonify({'status': 'error', 'message': 'Ошибка валидации формы!'})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




