
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

class PredictionForm(FlaskForm):
    jan = FloatField('January', validators=[DataRequired()])
    feb = FloatField('February', validators=[DataRequired()])
    mar = FloatField('March', validators=[DataRequired()])
    apr = FloatField('April', validators=[DataRequired()])
    may = FloatField('May', validators=[DataRequired()])
    jun = FloatField('June', validators=[DataRequired()])
    jul = FloatField('July', validators=[DataRequired()])
    aug = FloatField('August', validators=[DataRequired()])
    sep = FloatField('September', validators=[DataRequired()])
    oct = FloatField('October', validators=[DataRequired()])
    nov = FloatField('November', validators=[DataRequired()])
    dec = FloatField('December', validators=[DataRequired()])
#    annual_rainfall = FloatField('Annual Rainfall', validators=[DataRequired()])

    submit = SubmitField('Submit')