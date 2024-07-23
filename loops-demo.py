import random
number=random.randint(0,100)
hak=int(input("kaç hakkınız olmasını istersiniz: "))
#randıom sayıyı bulma
counter=0
puan=100
tahmin=int(input("0-100 arası bir sayıyı tahmin ediniz: "))
while hak>0:
    counter+=1
    hak-=1

    if tahmin>number:
        print("tutmadı lütfen aşağı ininiz")
    elif tahmin<number:
        print("tutmadı lütfen yukarı çıkınız")
    else:
        print("Tebrikler sonucu buldunuz sonuc: ",tahmin)
        print("Sonucu {} denemede buldunuz".format(counter))
        puan=puan-((counter-1)*20)
        print(f"puanınız: {puan}")
        break
    
    tahmin=int(input("sayıyı tahmin ediniz: "))
    print(f"kalan can sayısı: {hak}")
    if hak==0:
        print(f"Hakkınız bitti. Tutulan sayı: {number}")



