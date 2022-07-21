from flask_wtf import Form
from wtforms import TextField,IntegerField,TextAreaField,SubmitField,RadioField,SelectField
from wtforms import validators,ValidationError
class ContactForm(Form):
    name=TextField('Name',[validators.Required('enter your name')])
    Age=IntegerField('age')
    Address=TextAreaField('address')
    language=SelectField('Language',choices=[('cc','c++'),('py','python')])
    Gender=RadioField('gender',choices=[('m','male'),('f','female')])
    submit=SubmitField('Send')