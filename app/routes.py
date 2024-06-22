import os
import time
from flask import request, flash, render_template, jsonify, url_for, redirect
from werkzeug.utils import secure_filename
from app.forms import ImageForm
from app import app, ml
import uuid

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def uid():
        return str(uuid.uuid4())

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
                filename = uid() + file.filename[-4:]
                filepath = os.path.join(os.getcwd(), 'app', 'static', filename)
                file.save(filepath)
                selected_method = request.form['methodSelect']
                if selected_method == 'DETR':
                        obr = ml.show_detected_image(filepath, 'd')
                elif selected_method == 'YOLO':
                        obr = ml.show_detected_image(filepath, 'y')
                flash('GOOd', 'success')
                return render_template('image.html', filename=obr, path=os.getcwd())
        flash('Недопустимый тип файла!', 'error')
        return jsonify({'status': 'error', 'message': 'Bad type!'})

    flash('Ошибка валидации формы!', 'error')
    return jsonify({'status': 'error', 'message': 'Smth wrong with form!'})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




