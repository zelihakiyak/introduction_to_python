message='hello there. my name is zeliha whats up'
#message=message.upper() #tüm harfleri büyük harfe dönüştürür
#message=message.lower() #tüm harfleri küçük harfe dönüştürür
#message=message.title() #tüm kelimelerin ilk harfini büyük harfe dönüştürür
#message=message.capitalize() #stringin ilk harfini büyük harfe dönüştürür
#message=message.strip() #stringin başında varsa boşlukları yok eder
#message=message.split() #her bir kelimeyi ayrı str dönüştürüp dizi olarak yazdırır
#message=message.split('.') #noktadan önce sonrayı bütün şekilde str dönüştürür
"""message=message.split()
message='---'.join(message)""" #her kelimenin arasına belirtilen karakteri yerleştirir
"""index=message.find('sadık')
print(index)""" #çıkan index değeri pozitif ise aranan str içerisinde mevcuttur negatif çıktı verirse yok demektir
"""isFound=message.startswith('h') 
print(isFound)""" #ifadeye hangi harfle başlandığını sora ve t veya f söyler
""" isFound=message.endswith('k')
print(isFound)""" #ifadenin harfle bittiğini sorar ve t veya f söyler
#message=message.replace('zeliha','denizkızı') #ilk girilen stryi bulur ve onu ikinci kelimeye dönüştürerek değiştirir.
message=message.center(50,'*') #verilen ilk değer kadar karakter ayırır ve boşlukları girilen ikinci değerle doldurur
print(message)
