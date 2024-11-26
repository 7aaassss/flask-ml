import os
from flask import request, flash, render_template, jsonify
from app.forms import ImageForm
from app import app, ml
import uuid

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def uid():
        return str(uuid.uuid4())

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST', 'GET'])
def index():
    form = ImageForm()

    if request.method == 'POST':
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
                    filepath = os.path.join(os.path.dirname(__file__), 'static', filename)
                    file.save(filepath)
                    selected_method = request.form['methodSelect']
                    if selected_method == 'DETR':
                            obr = ml.show_detected_image(filepath, 'd')
                    elif selected_method == 'YOLO':
                            obr = ml.show_detected_image(filepath, 'y')
                    flash('GOOd', 'success')
                    return render_template('image.html', filename=obr)
            flash('Недопустимый тип файла!', 'error')
            return jsonify({'status': 'error', 'message': 'Bad type!'})

        flash('Ошибка валидации формы!', 'error')
        return jsonify({'status': 'error', 'message': 'Smth wrong with form!'})

    return render_template('index.html', form=form)
