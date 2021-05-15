from flask import Flask, flash, render_template, redirect, url_for 

app = Flask(__name__)
app.secret_key="abcdef"

@app.route("/")
def index():
     flash("index sayfasını açtınız", "error")
     return redirect(url_for('page1')) 
                          
@app.route("/page1")
def page1():
     flash("page1 sayfasını açtınız")
     return render_template("page.html")

@app.route("/page2")
def page2():
     return render_template("page2.html")
     
if __name__ == "__main__":
     app.run(debug=True)
