import random
alt=0
ust=100
sayi=random.randint(alt,ust)
answer=101
counter=0
while answer!=sayi:
    answer=int(input("Lütfen sayıyı tahmin ediniz [{},{}]:".format(alt,ust)))
    counter+=1
    if answer>sayi:
        print("Tutmadı biraz aşağı inin!!")
        ust=answer
    elif answer<sayi:
        print("Tutmadı biraz yukarı çıkın!!!")
        alt=answer
print("Tebrikler sonucu buldunuz sonuc: ",answer)
print("Sonucu {} denemede buldunuz".format(counter))