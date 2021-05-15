from flask import Flask

app = Flask(__name__)

@app.route("/")
def main_page():
     return "<h4><center>Ana Sayfa</center></h4>"

@app.route("/info")
def info():
     return "<h2><b>Test Sayfası</b></h2>"

if __name__ == "__main__":
     #app.run()
     app.run(debug=True)
     
