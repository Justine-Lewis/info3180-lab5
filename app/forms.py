# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired

#MovieForm class, Accepts only jpg,jpeg,png files to be uploaded
class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired()])
    description = TextAreaField('Description',validators=[InputRequired()])
    poster = FileField(
        'Movie Poster',
        validators =[FileRequired(), FileAllowed(['jpg', 'jpeg','png'],'Only Images Allowed!')
        ])
    #submit = SubmitField('Submit')


    

    