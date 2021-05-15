
from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def main_page():
     return render_template("all_pages.html", yaz="Ana Sayfa")

@app.route("/test")
def test():
     return render_template("all_pages.html", yaz="Test Sayfası")

@app.route("/page/<name>")
def page(name):
     return render_template("all_pages.html", yaz=name) 

@app.route("/page2/<name>-<int:year>")
def page2(name, year):
     #name_old = "{} {} yaşında.".format(name, 2021 - year)
     return render_template("kontrol.html", name=name, year=year)



     
