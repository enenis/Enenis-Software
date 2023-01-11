import sqlite3
con=sqlite3.connect("kütüphane.db")
cursor=con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa INT)")
    con.commit()
tablo_olustur()
def veri_ekle():
    cursor.execute("Insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

def kullanici_veri(isim,yazar,yayinevi,sayfa):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste= cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri...")
    for i in liste:
        print(i)
def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    liste=cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri...")
    for i in liste:
        print(i)
def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi=?",(yayınevi,))
    liste=cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri...")
    for i in liste:
        print(i)
def verileri_güncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("Update kitaplık set Yayınevi=? where Yayınevi=?",(yeni_yayınevi,eski_yayınevi))
    con.commit()
def verileri_sil(isim):
    cursor.execute("Delete From kitaplık where İsim=?",(isim,))
    con.commit()
verileri_sil("Kırmızı Diş")
con.close()
