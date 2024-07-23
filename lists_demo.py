#1. "bmw,mercedes,opel,mazda" elemanlarına sahip bir liste oluşturunuz.
brands=["bmw","mercedes","opel","mazda"]
print(brands) 

lenght=len(brands) #liste kaç elemanlıdır?
print(lenght)

print(brands[0],brands[lenght-1]) #listenin ilk ve son elemanı nedir?

brands[-1]='toyota' #mazda değerini toyota ile değiştir.
print(brands)

result= 'mercedes' in brands  #mercedes listenin bir elemanı mıdır?
print(result)

print(brands[-2]) #listenin -2. değerini verir

print(brands[0:3]) #listenin ilk üç değerini verir

brands[-2:]=["toyota","renault"] #listenin son iki değerini istediğinle değiştirirsin
print(brands)

yeniliste=brands+['audi','nissan'] #arabalar listesine yeni eleman ekleme için
print(yeniliste)

del brands[-1] #listenin son elemanını siler
print(brands)

print(brands[::-1]) #listeyi tersten yazdırır

studentA=['Yiğit','Bilgi',2010,[70,60,70]]
studentB=['Sena','Bilgi',1999,[80,80,70]]
studentC=['Ahmet','Turan',1998,[80,70,90]]
total=studentA+studentB+studentC #listedeki elemanları yazdırır

#Yiğit Bilgi 9 yaşında ve not ortalaması ... yazdır
result=f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
print(result)
