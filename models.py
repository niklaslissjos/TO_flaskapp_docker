#import datetime
#from app import db
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

# # this class not used for now
# class Post(db.Model):
#     __tablename__ = 'posts'
#
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String, nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False)
#
#     def __init__(self, text):
#         self.text = text
#         self.date_posted = datetime.datetime.now()

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=1, max=2)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=1, max=5)])
    submit = SubmitField('Send')

class SubscribeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send')
