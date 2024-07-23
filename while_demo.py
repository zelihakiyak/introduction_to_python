# sayilar=[1,3,5,7,9,12,19,21]
# i=0
# while (i<len(sayilar)):
#     print(sayilar[i])
#     i+=1

# i=100
# while i>0:
#     print(i)
#     i-=1

# numbers=[]
# i=0
# while i<5:
#     sayi=int(input("sayı: "))
#     numbers.append(sayi)
#     i+=1

# numbers.sort()
# print(numbers)

urunler=[]
x=int(input("ürün sayısı giriniz: "))
i=0
while i<x:
    name=input("ürünün adını giriniz: ")
    price=input("ürünün fiyatını giriniz: ")
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1

for urun in urunler:
    print(f"ürünün adı: {urun['name']} ürünün fiyatı: {urun['price']}")
    