from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, SelectField
from wtforms.validators import DataRequired

class ImageForm(FlaskForm):
    file = FileField('File', validators=[DataRequired()])
    methodSelect = SelectField('Method', choices=[('DETR', 'DETR'), ('YOLO', 'YOLO')], validators=[DataRequired()])
    submit = SubmitField('Upload')
