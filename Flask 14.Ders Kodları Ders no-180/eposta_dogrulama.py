from flask import Flask, render_template, url_for, request, redirect, flash
from my_form import nForm, pForm
from flask_mail import Mail, Message
from random import randint
import os

app = Flask(__name__)
app.config.from_object("config_class.Dev_Config")
mail=Mail(app)

images = os.listdir(app.config['UPLOAD_FOLDER'])

@app.route("/", methods=["GET","POST"])
def index():
     global dkod
     form = nForm()
     if form.validate_on_submit():
          dkod = str(randint(10000, 99999))
          eposta = form.eposta.data
          imaj  = form.img.data
          send_mail(eposta, imaj)
          return redirect(url_for('kontrol'))
     else:
          return render_template("index.html", form=form, images=images)
     
@app.route("/kontrol", methods=["GET","POST"])
def kontrol():
     form = pForm()
     renk="blue"
     if form.validate_on_submit():
          kod=form.kod.data
          if kod == dkod:
               flash("Doğrulama Gerçekleşti.")
          else:
               flash("Hatalı Kod.")
               renk="red"
          return render_template("kontrol.html", form=form, renk=renk)
     else:
          return render_template("kontrol.html", form=form, renk=renk)

def send_mail(eposta, imaj):
     msg = Message(
          subject="Password request",
          #sender='x.admns@gmail.com'
          recipients=[eposta])
     msg.body = "Merhaba {} Eposta doğrulama kodunuz: {}".format(eposta.split("@")[0], dkod)
     with app.open_resource(app.config['UPLOAD_FOLDER']+"/"+ imaj) as f:
          content = f.read()
     msg.attach(imaj,"image/png", content)  
     mail.send(msg)
        
if __name__ == "__main__":
     app.run()
