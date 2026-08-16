"""
ALIŞTIRMA 01 — Python Temelleri (Değişkenler + Koşullar + Döngüler)
Çalıştırmak için terminalde: python alistirma_01_python_temelleri.py
Her görevi tamamla, yorumları (#) sil ve kodu yaz.
"""

# ---------------------------------------------------------------
# GÖREV 1: Kendini tanıt
# 'isim' ve 'yas' adında iki değişken oluştur, sonra ekrana yazdır:
# "Ben <isim>, <yas> yaşındayım."  (f-string kullan)
# ---------------------------------------------------------------

isim = input("isminiz: ") 
yas = int(input("yasiniz: "))

print(f"Ben {isim}, {yas} Yasindayim")



# ---------------------------------------------------------------
# GÖREV 2: Basit parola kontrolü
# Kullanıcıdan input() ile şifre iste.
# Şifre "acilsusam" ise "Kapı açıldı 🔓" yazdır, değilse "Reddedildi 🔒".
# ---------------------------------------------------------------

sifre = input("Sifreniz: ")

if sifre == "acilsusam":
    print("Kapi Acildi 🔓")
else:
    print("Reddedildi🔒")


# ---------------------------------------------------------------
# GÖREV 3: Geri sayım
# for ve range() kullanarak 5'ten 1'e kadar geri say, sonunda "Başla!" yaz.
# İpucu: range(5, 0, -1)  -> 5,4,3,2,1
# ---------------------------------------------------------------

print("Geri Sayim Basliyor")
for x in range(5 , 0 , -1):
    print(x)
print("Basla")


# ---------------------------------------------------------------
# BONUS (biraz zorlayıcı): 3 deneme hakkı olan şifre ekranı
# while döngüsü + sayaç kullan. Doğru şifre "1337".
# Kullanıcı 3 kez yanlış girerse "Hesap kilitlendi" yaz ve dur.
# Doğru girerse "Giriş başarılı" yaz ve döngüden çık (break).
# ---------------------------------------------------------------

# buraya yaz
