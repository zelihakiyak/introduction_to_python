def square(num): return num**2
numbers=[1,3,5,9]
result=map(square,numbers)  #bellek üzerinde bir adresi gönderir
result=list(map(square,numbers))#değerleri liste içinde çıktı verir
print(result)  #map bir built-in fonksiyon
#alternatif olarak for döngüsü de kullanılabilir.
for item in map(square,numbers):
    print(item)

#fonksiyonu ayrı bir yerde tanımlamak yerine 
#isimsiz bir fonksiyon kullanabilirim
result=list(map(lambda num: num**2, numbers))
print(result)
#ya da şu şekilde kullanılabilir
square=lambda num: num**2
result=square(4)
print(result)
################################
numbers=[1,3,5,9,10,4]
def check_even(num): return num%2==0
result=list(filter(check_even,numbers))
#ya da şu şekilde
result=list(filter(lambda num: num%2==0, numbers))
print(result)

