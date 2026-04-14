# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired

#UploadForm class, Accepts only jpg,jpeg,png files to be uploaded
class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description',validators=[InputRequired()])
    poster = FileField(
        'Upload An Image',
        validators =[FileRequired(), FileAllowed(['jpg', 'jpeg','png'],'Only Images Allowed!')
        ])
    #submit = SubmitField('Submit')


    

    