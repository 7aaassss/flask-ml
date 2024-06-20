import os
import time

from flask import request, flash, render_template, jsonify, url_for, redirect
from werkzeug.utils import secure_filename
from app.forms import ImageForm
from app import app
from app import ml
import uuid

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def uid():
        return str(uuid.uuid4())

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ImageForm()
    return render_template("index.html", form=form)


if file and allowed_file(file.filename):

            filename = uid() + file.filename[-4:]

            filepath = os.path.join(os.getcwd(), filename)

            file.save(filepath)

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




