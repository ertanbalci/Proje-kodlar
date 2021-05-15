from flask import Flask, abort, redirect, make_response, request, url_for

app = Flask(__name__)

# root (index) view fonksiyonu
@app.route("/")
def index():
     return "<h3><center> Merhaba Kullanıcı </center></h3>"

# Admin'in parola ile giriş yapacağı sayfanın view fonksiyonu
@app.route("/admin/<password>")
def admin(password):
     deneme = request.cookies.get("deneme") # none döndürür veya deneme sayısını döndürür
     if not deneme:
          deneme=1
     if password=="1234":
          return "<h2><b> Admin Sayfası </b></h2>"
     if int(deneme)>3:
          return redirect(url_for("honey_pot", password=password))
     else:
          response = resp_objesi_hazırla(deneme)
          return response

# Sadece hatalı parola girildiğinde hatalı parola girildiğini bildirmek amacıyla
# response objesi oluşturup view fonksiyonuna gönderir.
def resp_objesi_hazırla(deneme):
     response = make_response("<h1>Hatalı Parola {} kez </h1>".format(deneme))
     response.set_cookie("deneme", str(int(deneme)+1), max_age= 60 * 60)
     return response

# Şüpheli giriş takibi (log kaydı)
@app.route("/honey_pot/<password>")
def honey_pot(password):
     user_ip = request.environ.get("HTTP_X_REAL_IP", request.remote_addr)
     deneme2 = request.cookies.get("deneme")
     mesaj = "\nŞüpheli {} {} kez hatalı parola ( {} ) girdi>\n".format(user_ip, deneme2, password)
     if int(deneme2)>6:
          print(mesaj+ "Abort 401 uygulandı.")
          abort(401)
     else:
          print(mesaj)
          response = resp_objesi_hazırla(deneme2)
          return response

# Hatalı deneme sayısı 6'yı geçtiğinde çerez ömrü(60*60) 1 saat boyunca giriş yapamayız.
# Test ortamında denemeler esnasında 1 saat bekleyemeyiz.
# Test ortamında çerezi resetlemek için bir backdoor view fonksiyonu yazıyoruz.
# Uygulama gerçek ortama taşınırkeb böyle backdoor view fonksiyonlar silinmelidir.
@app.route("/pr")
def pasw_reset():
     mesaj = "Parola deneme sayısını gösteren çerez resetlendi."
     print("\n"+ mesaj + "\n")
     response = make_response(mesaj)
     response.delete_cookie("deneme")
     return response

if __name__ == "__main__":
     app.run(debug=True)
     
     
     
     
          
