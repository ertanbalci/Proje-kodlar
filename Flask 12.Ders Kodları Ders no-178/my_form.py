from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired 

class LoginForm(FlaskForm):
     name = StringField("Kullanıcı Adı" ,validators=[InputRequired()])
     submit = SubmitField("Gönder") 

     
     
