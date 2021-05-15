from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/uploaded_images"
app.config['UPLOAD_EXTENSIONS'] = [".jpg", ".jpeg", ".png"]
app.config['SECRET_KEY'] = "dosya yükleme xx11233"

dosyalar=""
for uzanti in app.config['UPLOAD_EXTENSIONS']:
    dosyalar = dosyalar + " "+ uzanti
info = "Sadece {} uzantılı dosyalar yüklenir.".format(dosyalar)
    
@app.route("/")
def index():
    return render_template("index.html", info=info)

@app.route("/file_upload", methods=["GET", "POST"])
def file_upload():
    if request.method == 'POST':
        dosya = request.files['imaj']

        # Dosya yüklemeden gönder butonuna basılırsa
        if not dosya:
            flash("Lütfen önce yüklenecek dosyayı seçin")
            return redirect(url_for("index")) 

        # Dosya adının güvenliğini sağlama / dosya_adi = dosya.filename
        dosya_adi=secure_filename(dosya.filename)

        #uzantı kontrolü
        uzanti = os.path.splitext(dosya_adi)[1].lower()
        if uzanti not in app.config['UPLOAD_EXTENSIONS']:
            flash("{} uzantılı dosyalar yüklenemez.".format(uzanti))
            return redirect(url_for("index"))
        dosya.save(os.path.join(app.config['UPLOAD_FOLDER'], dosya_adi))
        return redirect('uploaded_files/' + dosya_adi)
    else:
        return "<h2><font color='red'>Yetkisiz erişim</font><h2>", 401
        
@app.route("/uploaded_files/<string:dosya_adi>")
def uploaded_files(dosya_adi):
     return render_template("goster.html", dosya_adi=dosya_adi)

@app.route("/show_images")
def show_images():
     images = os.listdir(app.config['UPLOAD_FOLDER'])
     return render_template('show_images.html', images=images)

if __name__ == "__main__":    
     app.run(debug=True)
     
