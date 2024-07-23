#1.Ehliyet alma durumunu kontrol ediniz.
# name=input("isminiz: ")
# age=int(input("yaşınız: "))
# statu=input("eğitim durmunuz: ")

# if (age>=18) and (statu=='lise' or statu=='üniversite'):
#     print("ehliyet alabilir")
# else:
#     print("ehliyet alamaz")

#2.Not hesaplama
# sınav1=float(input("ilk yazılı notunu gir: "))
# sınav2=float(input("son yazılı notunu gir: "))
# sozlu=float(input("sözlü notunu gir: "))
# ortalama=(sınav1+sınav2+sozlu)/3
# if 0<=ortalama<=24:
#     print("notunuz: 0")
# elif 24<ortalama<=44:
#     print("notunuz: 1")
# elif 44<ortalama<=54:
#     print("notunuz: 2")
# elif 54<ortalama<=69:
#     print("notunuz: 3")
# elif 69<ortalama<=84:
#     print("notunuz: 4")
# elif 84<ortalama<=100:
#     print("notunuz: 5")
#else:
#     print("yanlış bilgi girdiniz.")

#3.Aracın servis zamanı hesapla

# import locale
# locale.setlocale(locale.LC_ALL, 'turkish')
# import datetime
# simdi=datetime.datetime.now()
# print(simdi)
# tarih=input("Aracın tarfiğe çıktığı tarihi string olarak gün,ay,yıl formatıyla giriniz: ")
# aracTarihi=datetime.datetime.strptime(tarih, '%d %B %Y')
# print(aracTarihi)
# fark=simdi-aracTarihi
# gun=fark.days
# print(gun)
# if gun<=365:
#     print("1.servis aralığı")
# elif (gun>365) and (gun<=365*2):
#     print("2.servis aralığı")
# elif (gun>365*2) and (gun<=365*3):
#     print("3.servis aralığı")
# else:
#     print("hatalı süre")

#1.Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# sayi=float(input())
# if 0<=sayi<=100:
#     print("sayı 0-100 arasındadır")
# else:
#     print("sayı 0-100 arasında değildir")

#2.Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# sayi=int(input("sayı: "))
# if sayi>0:
#     if sayi%2==0:
#         print("sayı pozitif bir çift sayıdır.") 
#     else:
#         print("sayı pozitif bir tek sayıdır.") 
# else:
#      print("sayı pozitif bir çift sayı değildir.")    


#3.Email ve parola bilgileriyle giriş kontolü yapınız.
# email="zelihakyk64.43@hotmail.com"
# password='141414'
# eposta=input("epostanızı giriniz: ")
# sifre=input("şifrenizi giriniz: ")

# if (eposta.strip()==email):
#     if (sifre.strip()==password):
#         print("Eposta adresiniz ve parola doğrudur")
#     else:
#         print("Girdiğiniz parola yanlıştır.")
# else:
#     print("Girdiğiniz eposta ve şifre yanlıştır.")

#4.Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# sayi1=int(input())
# sayi2=int(input())
# sayi3=int(input())
# if (sayi1>sayi2) and (sayi1>sayi3):
#      print(f"En büyük sayı:{sayi1}")
# elif (sayi2>sayi1) and (sayi2>sayi3):
#      print(f"En büyük sayı: {sayi2}")
# elif (sayi3>sayi1) and (sayi3>sayi2):
#      print(f"En büyük sayı:{sayi3}")

#5.Kullanıcıdan 2 vize notu (%60)ve final notu(%40) alıp ortalama hesaplayınız
#eğer ortalama 50 ve üzeri ise geçti ya da kaldı yazdırınız
# vize1=int(input("Vize1notunuzu giriniz:"))
# vize2=int(input("Vize2 notunuzu giriniz:"))
# final=int(input("Final notunuzu giriniz:"))
# result=(((vize1+vize2)/2)*0.6)+(final*0.4)

# if result>50:
#     if final>=50:
#         print(f"Ortalamanız: {result} ve geçme durumu başarılı")
#     else:
#         print(f"Ortalamanız: {result} ve geçme durumu başarısız")
# else:
#     print("Üzgünüz kaldınız")

#6.
ad=input("Adınızı girin: ")
kilo=float(input("Kilonuzu giriniz: "))
boy=float(input("Boyunuzu m cinsinden giriniz: "))
indeks=(kilo/(boy**2))
if 0<=indeks<=18.4:
    print("zayıfsınız")
elif 18.4<indeks<=24.9:
    print("normal")
elif 24.9<=indeks<=29.9:
    print("fazla kilolu")
elif 29.9<=indeks<=34.9:
    print("şişman(obez)")
else:
    print("Girdiğiniz bilgiler yanlış")






















