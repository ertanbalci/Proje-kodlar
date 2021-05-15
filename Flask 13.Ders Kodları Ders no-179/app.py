from flask import Flask, render_template, url_for, request
from my_form import nForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "csrf için gizli anahtar"
app.config['RECAPTCHA_PUBLIC_KEY'] = "6Lef22AaAAAAAGj50R3Y8M30a0JC_lltBWb6er-F"
app.config['RECAPTCHA_PRIVATE_KEY'] = "6Lef22AaAAAAAFyovnYXRTCUqh3Nzo_FstE6Z3kN"

@app.route("/")
def index():
     return render_template("index.html")
          
@app.route("/login", methods=["GET","POST"])
def login():     
     form = nForm()
     if form.validate_on_submit():
          information=dict()
          information["Adı"]=form.adi.data+" "+ form.s_adı.data
          information["Yaşı"]=form.yas.data
          information["Cinsiyeti"]=form.cns.data
          information["Egitim"]=form.egitim.data
          information["Mezuniyet Tarihi"]=form.mt.data
          information["e-posta"]=form.eposta.data
          information["Adres"]=form.adres.data
          information["Parola"]=form.parola.data
          information["KVK Kabul"]=form.kvk.data
          return render_template("kayitGoster.html", information=information)
     else:
          return render_template("yeni.html", form=form)
     
if __name__ == "__main__":
     app.run(debug=True)
