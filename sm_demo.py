website="http://www.zelihakiyak.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40saat)"

#1.'Hello world' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result='Helloworld'.strip()
result='hello world'.lstrip() #strnin solundan silmek için kullanılır
result='helloworld'.rstrip() #strnin sağından silmek için kullanılır
print(result)

#2.'www.zelihakiyak.com' içindeki zelihakiyak bilgisi haricindeki her karakteri silin.
result=website.strip('htps:/w.com')
print(result)

#3.'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result=course.lower()
print(result)

#4. 'website' içinde kaç tane a karakteri vardır?
result=website.count('a') 
r=website.count('www',0,10) #verilen aralıkta bakılır (0. ile 10.karaktert arası)
print(result)
print(r)

#5. 'website' "www" ile başlayıp com ile bitiyor mu?
isFound=website.startswith('www')
print(isFound)
isFound=website.endswith('com')
print(isFound)

#6.'website' içinde '.com' ifadesi var mı?
result=website.find('.com')
#result=website.find('.com',0,10) # aralıkta o ifade var mı kontrol eder
print(result) #index numarasını verir.
result=course.rfind('Python') #sağdan sola aramaya başlar.
result=website.index('.com') #index numarası negatif değilse mevcut demektir
result=website.rindex('.com')

#7. 'course' içindeki harflerin hepsi alfabetik mi? (isalpha, isdigit)
result=course.isdigit()
print(result)

#8.'contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result='contents'.center(50,'*')
result='contents'.ljust(50,'*') #yazıyı sola yatırır
result='contents'.rjust(50,'*') #yazıyı sağa yatırır
print(result)

#9.'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
result=course.replace(' ','-')
print(result)

#10. 'hello world' karakter dizisinin 'world' ifadesini 'there' olarak değiştirin
result='hello world'.replace('world','there')
print(result)

#11. 'course' dizisini boşluk karakterlerinden ayırın
result=course.split(' ')
print(result)