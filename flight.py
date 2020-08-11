from flask_wtf.form import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import data_required,Email,length,EqualTo


class registerform(FlaskForm):
    flight_name=StringField("Flight name: ")
    flight_code=StringField("Flight code: ")
    flight_city=StringField("Enter city:  ")
    submit = SubmitField("Register")