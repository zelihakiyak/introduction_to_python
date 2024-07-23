def topla (liste):
    even=0
    odd=0
    
    for index in range(len(liste)):
        if liste[index]%2==0:
            even+=liste[index]
        if liste[index]%2!=0:
            odd+=liste[index]
    newlist=[even,odd]
    return newlist

liste=[]

"""for i in range(6):
    x=int(input("bir sayı giriniz: "))
    liste.append(x)"""

while True:
    x=int(input("bir sayı giriniz(çıkış içi -1 giriniz.): "))
    if x==-1:
        break
    liste.append(x)
    
print(liste)
print(topla(liste))

    