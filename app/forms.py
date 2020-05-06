from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired

class CsvForm(FlaskForm):
    datasheet = FileField('CSV Dataset', validators=[DataRequired()])
    datatype = StringField('classification or regression?', validators=[DataRequired()])
    submit = SubmitField('Process')
    
class PredictForm(FlaskForm):
    datasheet = FileField('CSV Dataset', validators=[DataRequired()])
    submit = SubmitField('Predict')
