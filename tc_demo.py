#yarı çapı verilen bir dairenin alan ve çevresini hesaplayın(pi=3.14
#daire alanı: pirekare
#daire çevresi: ikipire

r=float(input("dairenin yarıçapı:")) #input str değer verir
# r= float(r)
dairealani=3.14*r**2
dairecevresi=2*3.14*r
print("Alan: ", dairealani)
print("Çevre: ", dairecevresi)