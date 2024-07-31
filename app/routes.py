from flask import render_template,url_for,flash
from app import app
from app.forms import PredictionForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/prediction')
def prediction():
    form = PredictionForm()
##needto add the form submitting & giving result part here based on part 3 in miguelblog

    return render_template('prediction.html',title='Prediction' , form=form)

@app.route('/results')
def results():
    return render_template('results.html',title='Results')

@app.route('/visualisations')
def visualisations():
    return render_template('visualisations.html',title='Graphs')