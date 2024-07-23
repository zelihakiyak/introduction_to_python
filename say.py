while True:
 
    # Kullanıcıdan bir sayı girmesini iste
    sayi=(input("Bir sayı girin (Çıkış için -1): "))

    # -1 girildiyse döngüyü sonlandır
    if int(sayi) == -1:
        print("Programdan çıkılıyor...")
        break

    # Girilen sayının basamak sayısını hesapla
    counter=0
    for i in sayi:
        counter+=1
    print(f"girdiğiniz sayı {counter} basamaklıdır")

   