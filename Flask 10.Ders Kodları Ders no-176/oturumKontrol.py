from flask import Flask, session, flash, abort, request,  render_template, redirect, url_for 

app = Flask(__name__)
#app.secret_key = "gizli anahtar karmaşık ve tahmine edilemez olmalı"
app.config["SECRET_KEY"] = "gizli anahtar karmaşık ve tahmine edilemez olmalı"

@app.route("/")
def index():
     if "user" in session:
          return redirect(url_for('page'))
     return redirect(url_for('login')) 

@app.route("/login", methods=["GET", "POST"])
def login():
     error = None
     if request.method=="POST":
          session["user"]= request.form["user"]
          session["mail"]= request.form["mail"]
          if session["user"]:
               return redirect(url_for('page')) 
          else:
               error= "Kimsiniz?"
     return render_template("login.html", error=error)
                          
@app.route("/page")
def page():
     if "user" in session:
          user=session["user"]
          return render_template("page.html", user=user)
     else: abort(401) 

@app.route("/logout")
def logout():
     session.clear()
     flash("Çıkış yaptınız")
     return redirect(url_for('index'))
     
if __name__ == "__main__":
     app.run(debug=True)

