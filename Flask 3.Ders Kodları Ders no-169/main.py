from flask import Flask

app = Flask(__name__)

@app.route("/")
def main_page():
     return "<h4><center>Ana Sayfa</center></h4>"

@app.route("/info")
def info():
     return "<h2><b>Test Sayfası</b></h2>"

@app.route("/page/<name>")
def page(name):
     return "Merhaba {}".format(name)

@app.route("/page2/<name>-<int:year>")
def page2(name, year):
     old = 2021 - year
     return "{} {} yaşında".format(name, old)
     
