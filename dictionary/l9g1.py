def kontrol(dict, klasor1, klasor2):
    if klasor1 not in dict or klasor2 not in dict:
        return False
    
    alt_klasorler = dict[klasor2]
    while alt_klasorler:
        alt_klasor = alt_klasorler.pop()
        if alt_klasor == klasor1:
            return True
        if alt_klasor in dict:
            alt_klasorler.extend(dict[alt_klasor])

    return False

   
dict={'a':{'b':{'e':1,'f':1,},'c': 1,'d':{'g':{'ı':1,'j':1},'h':{'k':1}}}}

while True:
    x=input('')
    if x=='q':
        break

    klasor1, klasor2 = x.split(',')
    sonuc = kontrol(dict, klasor1, klasor2)
    print(sonuc)