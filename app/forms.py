import os
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CsvForm(FlaskForm):
    datasheet = FileField('CSV Dataset', validators=[DataRequired()])
    datatype = StringField('classification or regression?', validators=[DataRequired()])
    submit = SubmitField('Process')
    
class PredictForm(FlaskForm):
    datasheet = FileField('CSV Dataset', validators=[DataRequired()])
    myModels = os.listdir('C:/Users/Matt/Documents/graymatter-flask/assets/models/')
    myChoices = []
    for model in myModels:
        myChoices.append((model,model))
    model_name = SelectField('Select the Model', choices = myChoices, validators=[DataRequired()])
    submit = SubmitField('Predict')
