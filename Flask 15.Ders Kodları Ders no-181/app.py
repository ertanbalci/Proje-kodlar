from flask import Flask, render_template, url_for, request
from my_form import nForm
import sqlite3

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
          adi   = form.adi.data
          s_adı = form.s_adı.data
          yas   = form.yas.data
          cns   = form.cns.data
          egt   = form.egitim.data
          mt    = form.mt.data
          ep    = form.eposta.data
          adr   = form.adres.data
          pw    = form.parola.data
          kvk   = form.kvk.data
          sonuç = verileri_kaydet(adi, s_adı, yas, cns, egt, mt, ep, adr, pw, kvk)
          return render_template("kayit_sonuç.html", sonuç=sonuç)
     else:
          return render_template("yeni.html", form=form)

def verileri_kaydet(adi, s_adı, yas, cns, egt, mt, ep, adr, pw, kvk):
     try:
          with sqlite3.connect("records.db") as vt:
               imleç = vt.cursor()

               sql = "INSERT INTO basvurular (adi, soyadi,yas, cinsiyet, egitim, \
                     mezuniyet_tarihi, eposta, adres, parola, kvk) VALUES \
                     (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
               
               imleç.execute(sql,(adi, s_adı, yas, cns, egt, mt, ep, adr, pw, kvk))
               vt.commit()
               sonuç = "+Başvuru Kaydedildi."
     except:
          vt.rollback()    
          sonuç = "-Başvuru kaydedilemedi"
     finally:
          return sonuç  

@app.route("/rec_list")
def rec_list():
     kayıt_listesi = []
     with sqlite3.connect("records.db") as vt:
          imleç = vt.cursor()
          sql = "SELECT adi, soyadi, cinsiyet, yas, egitim, eposta FROM basvurular"
          imleç.execute(sql)
          kayıt_listesi = imleç.fetchall()          
     return render_template("rec_list.html", kayıt_listesi=kayıt_listesi)
     
if __name__ == "__main__":
     app.run(debug=True)     
