from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
     sayfalar = [("html_tags", "Html"), ("text_tags", "Metin düzenleme"),
                 ("link_tags", "Link"), ("table_tags", "Tablo"),
                 ("form_tags", "Form")]
     return render_template("index.html", sayfalar=sayfalar)

@app.route("/htmltags")
def html_tags():
     dosya = read_text("text/page_tags.txt")
     return render_template("tags.html", dosya=dosya)

@app.route("/texttags")
def text_tags():
     dosya = read_text("text/text_tags.txt")
     return render_template("tags.html", dosya=dosya)

@app.route("/linktags")
def link_tags():
     dosya = read_text("text/link_tags.txt")
     return render_template("tags.html", dosya=dosya)

@app.route("/tabletags")
def table_tags():
     dosya = read_text("text/table_tags.txt")
     return render_template("tags.html", dosya=dosya)

@app.route("/formtags")
def form_tags():
     dosya = read_text("text/form_tags.txt")
     return render_template("tags.html", dosya=dosya)

def read_text(file):
     with open(file, "r")as f:
          return f.readlines()

if __name__ == "__main__":
     app.run(debug=True)
