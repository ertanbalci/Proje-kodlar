
from flask import Flask , render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
     return  render_template("index.html")

@app.route("/kayitFormu")
def kayitFormu():
     return render_template("yeniKayit2.html")

@app.route("/kayitKontrol", methods=["POST", "GET"]) 
def kayitKontrol():
     if request.method=="POST":
          basvuru=request.form
          return render_template("kayitGoster.html", basvuru=basvuru)
    
if __name__ == "__main__":  
     app.run(debug=True)   

