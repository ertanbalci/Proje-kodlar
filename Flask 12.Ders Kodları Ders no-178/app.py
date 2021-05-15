from flask import Flask, render_template, url_for
from my_form import LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "csrf için gizli anahtar" 

@app.route("/")
def index():
     return render_template("index.html")
          
@app.route("/login", methods=["GET","POST"])
def login():
     form = LoginForm()
     if form.validate_on_submit():
          name = form.name.data
          return render_template("kGoster.html", name=name)          
     return render_template("login_page.html", form=form)

if __name__ == "__main__":
     app.run(debug=True)
