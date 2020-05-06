import os
from app import app
from flask import render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from app.forms import CsvForm, PredictForm
from app.EasyAI import easy_ai

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Matt'}
    accuracies = [
            {
                    'model': 'K Nearest',
                    'accuracy' : 0.84
                    },
            {
                    'model': 'SVM RBF Kernel',
                    'accuracy': 0.93
                    }
            ]
    return render_template('index.html', user=user, accuracies=accuracies)

@app.route('/processdata', methods=['GET', 'POST'])
def processdata():
    form = CsvForm()
    if form.validate_on_submit():
        flash('Analysis requested for dataset {}, datatype={}'.format(form.datasheet.data.filename, form.datatype.data))
        assets_dir = os.path.join(os.path.dirname(app.instance_path), 'assets')
        
        csv = form.datasheet.data
        csv_filename = secure_filename(csv.filename)
        
        csv.save(os.path.join(assets_dir, 'tempdata', csv_filename))
        
        
        results_array = easy_ai.easyanalysis(csv_filename, form.datatype.data)
        os.remove('C:/Users/Matt/Documents/graymatter-flask/assets/tempdata/'+csv_filename)
        flash('Model Selected: {}\nAccuracy: {}'.format(results_array[0],results_array[1]))
        
        return redirect(url_for('index'))
    return render_template('processdata.html', title='Process Data', form=form)

@app.route('/predictdata', methods=['GET', 'POST'])
def predictdata():
    form = PredictForm()
    if form.validate_on_submit():
        assets_dir = os.path.join(os.path.dirname(app.instance_path), 'assets')
        
        input_data = form.datasheet.data
        input_filename = secure_filename(input_data.filename)
        
        input_data.save(os.path.join(assets_dir, 'tempdata', input_filename))
        
        results_array = easy_ai.prediction(input_filename, model)
        
        os.remove('C:/Users/Matt/Documents/graymatter-flask/assets/tempdata/'+input_filename)
        return redirect(url_for('results', results_arr=results_array))
    return render_template()

@app.route('/results')
def results():
    return render_template("results.html", predicted_vals = request.args.get('results_arr'))