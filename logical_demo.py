#1.Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# sayi=float(input())
# result= 0<sayi<100
# print(result)

#2.Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# sayi=int(input())
# result= sayi>0 and sayi%2==0
# print(result)

#3.Email ve parola bilgileriyle giriş kontolü yapınız.
# email="email@gmail.com"
# password="56321"
# posta=input()
# parola=input()
# result= email==posta.split() and password==parola.split()
# print(result)

#4.Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# sayi1=int(input())
# sayi2=int(input())
# sayi3=int(input())
# if (sayi1>sayi2) and (sayi1>sayi3):
#     print(f"En büyük sayı:{sayi1}")
# elif (sayi2>sayi1) and (sayi2>sayi3):
#     print(f"En büyük sayı: {sayi2}")
# elif (sayi3>sayi1) and (sayi3>sayi2):
#     print(f"En büyük sayı:{sayi3}")

#5.
# vize1=float(input())
# vize2=float(input())
# final=float(input())
# ortalama=((vize1+vize2)/2)*0.6+(final*0.4)
# #result= ortalama>=50 and final>=50 #ilk koşul
# result=(ortalama>=50) or (final>=70)
# print(f"öğrencinin ortalaması: {ortalama} ve geçme durumu: {result}")
    
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
