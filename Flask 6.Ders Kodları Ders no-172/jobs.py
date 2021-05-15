from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def to_do_jobs():
     jobs =[ ['Alınan siparişler üretim hattına bildirilecek', '1'],
             ['İş başvuruları incelenecek',                    '3'],
             ['Performans prim değerlendirmesi yapılacak',     '2'],
             ['Fazla mesai planlaması yapılacak',              '2'],
             ['İade ürünler kontrol edilecek',                 '3'],
             ['Hammadde planlaması yapılacak',                 '1']  ] 
     return render_template("daily_jobs.html", today="26 Nisan 2021", jobs=jobs)

if __name__ == "__main__": 
     app.run(debug=True)
