from flask_wtf import FlaskForm

from wtforms import StringField, RadioField, SubmitField  

from wtforms.validators import InputRequired, Email
import os

images = os.listdir('./static/images')
class nForm(FlaskForm):
     eposta = StringField("e-posta adresiniz" ,
                          [InputRequired(),
                           Email(message="Geçersiz E-Posta Adresi")])
     img = RadioField("Seçtiğiniz Resim", [InputRequired()], choices=images)

     submit = SubmitField("E-posta adresime doğrulama kodu gönder")
     
class pForm(FlaskForm):
     kod = StringField("Doğrulama Kodu" ,[InputRequired()])
     
     submit = SubmitField("Gönder")
