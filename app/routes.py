from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import PredictionForm
import pickle
import pandas as pd
import os

# Load the trained model
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'utils', 'flood-model.pkl')
with open(model_path, 'rb') as file:
    clf = pickle.load(file)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    form = PredictionForm()
    if form.validate_on_submit():
        # Get the input data from the form
        jan = form.jan.data
        feb = form.feb.data
        mar = form.mar.data
        apr = form.apr.data
        may = form.may.data
        jun = form.jun.data
        jul = form.jul.data
        aug = form.aug.data
        sep = form.sep.data
        oct = form.oct.data
        nov = form.nov.data
        dec = form.dec.data
        
        # Calculate the annual rainfall
        monthly_rainfalls = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
        annual_rainfall = sum(monthly_rainfalls) / 12

        # Create a Pandas DataFrame from the input data
        new_data = pd.DataFrame({
            'JAN': [jan],
            'FEB': [feb],
            'MAR': [mar],
            'APR': [apr],
            'MAY': [may],
            'JUN': [jun],
            'JUL': [jul],
            'AUG': [aug],
            'SEP': [sep],
            'OCT': [oct],
            'NOV': [nov],
            'DEC': [dec],
            ' ANNUAL RAINFALL': [annual_rainfall]
        })

        # Make a prediction using the trained model
        prediction = clf.predict(new_data)
        label_mapping = {0: 'NO', 1: 'YES'}
        prediction_label = label_mapping[prediction[0]]

        # Flash the prediction result
        flash(f'Our Analysis: {prediction_label}')

    return render_template('prediction.html', title='Prediction', form=form)

@app.route('/visualisations')
def visualisations():
    return render_template('visualisations.html', title='Graphs')