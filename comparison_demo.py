# 1.Girilen sayıdan hangisi daha büyüktür?
# x=int(input())
# y=int(input())

# if x<y:
#     print(f"{y} sayısı büyüktür")
# else:
#     print(f"{x} sayısı daha büyüktür")

#2.Kullanıcıdan 2 vize notu (%60)ve final notu(%40) alıp ortalama hesaplayınız
#eğer ortalama 50 ve üzeri ise geçti ya da kaldı yazdırınız
# vize1=int(input("Vize1notunuzu giriniz:"))
# vize2=int(input("Vize2 notunuzu giriniz:"))
# final=int(input("Final notunuzu giriniz:"))
# result=(((vize1+vize2)/2)*0.6)+(final*0.4)
# print(f"Ortalamanız: {result}")
# if result>50:
#     print("Tebrikler geçtiniz")
# else:
#     print("Üzgünüz kaldınız")

#Girilen bir sayının tek mi 
# sayi=int(input())
# if sayi%2==0:
#     print("Girilen sayı çifttir.")
# else:
#     print("Girilen sayı tektir.")

#4.Girilen sayının pozitif ya da negatif olma durumunu yazdırın.
# sayi=int(input())
# isPositive=(sayi>0)
# print(f"Girilen sayının pozitif olma durumu: {isPositive}")

#5.
email="zelihakyk64.43@hotmail.com"
password='141414'
eposta=input("epostanızı giriniz: ")
sifre=input("şifrenizi giriniz: ")

is_email_correct= (eposta.strip()==email)
is_password_correct=(sifre.strip()==password)
print(f"Eposta adresinizin doğru olma durumu: {is_email_correct}")
print(f"Şifrenizin doğru olma durumu: {is_password_correct}")
