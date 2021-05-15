import sqlite3

vt = sqlite3.connect("records.db")

sql = "CREATE TABLE IF NOT EXISTS basvurular(adi TEXT, soyadi TEXT,\
yas INTEGER, cinsiyet TEXT, egitim TEXT, mezuniyet_tarihi TEXT, \
eposta TEXT, adres TEXT, parola TEXT, kvk INTEGER)"

vt.execute(sql)       
                             
vt.close()   
