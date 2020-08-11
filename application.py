from flask_wtf.form import FlaskForm
from wtforms import StringField,SubmitField

#from wtforms.validators import data_required


class registerform(FlaskForm):
    first_name=StringField("Enter First Name: ")
    middle_name=StringField("Enter middle name: ")
    last_name=StringField("Enter last name:  ")
    rel_name=StringField("Enter your religion: ")
    addr=StringField("Enter permanent address: ")
    gen=StringField("Enter your Gender: ")
    DOT=StringField("Enter Date of Birth: ")
    mobno=StringField("Enter mobile number: ")
    submit = SubmitField("Register")