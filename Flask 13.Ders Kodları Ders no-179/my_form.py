
from wtforms import StringField, IntegerField, RadioField, SelectField, \
     TextAreaField, PasswordField, BooleanField, SubmitField  

from wtforms.fields.html5 import DateField 

from wtforms.validators import InputRequired, Length, NumberRange, Optional, EqualTo, Email

from flask_wtf import FlaskForm, RecaptchaField

class nForm(FlaskForm):
     adi = StringField("Adınız" ,
                       [InputRequired(),
                        Length(min=3, message="İsim en az 3 karakter olmalı")])

     s_adı = StringField("Soyadınız" ,validators=[InputRequired()])
     
     yas = IntegerField("Yaşınız" ,
                        [InputRequired(),
                         NumberRange(min=7, max=130, message="Yaş aralığı 7-130")])
     
     cns = RadioField("Cinsiyetiniz", [Optional()], choices=[('E','Erkek'),('K','Kadın')])
     
     egitim = SelectField("Eğitim Durumunuz",
                          choices=["","İlkÖğretim", "Lise", "Üniversite",
                                   "Yüksek Lisans", "Doktora"])

     mt = DateField("Mezuniyet Tarihiniz", validators=[Optional()])

     eposta = StringField("e-posta adresiniz" ,[InputRequired(),
                                                Email(message="Geçersiz E-Posta Adresi")])

     adres = TextAreaField("Adresiniz" ,validators=[Optional()])

     parola = PasswordField("Parolanız", [InputRequired(),
                                          Length(min=8, max=16,
                                          message="Parola uzunluğu 8-16 karakter olmalı")])

     cparola = PasswordField("Parolanız Tekrar",
                             [EqualTo("parola", message="Girdiğiniz parolalar farklı")])
     
     kvk = BooleanField("Kurumunuzun KVK uygulamlarını kabul ediyorum.", default=False)

     recaptcha = RecaptchaField()

     submit = SubmitField("Gönder")

     
     
