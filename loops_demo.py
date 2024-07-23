# sayilar=[1,3,5,7,9,12,19,21]
# """for i in sayilar:
#     if i%3==0:
#         print(f"{i} sayısı üçün katıdır.") """
# toplam=0
# """for x in sayilar:
#     toplam+=x
# print(toplam)"""

# for a in sayilar:
#     if (a%2!=0):
#         print(f"{a} sayısının karesi= {a**2}")

# sehirler=['kocaeli','istanbul','ankara','izmir','rize']
# for x in sehirler:
#     if len(x)<=5:
#         print(x)

urunler= [
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S8','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'}
    ]
toplam=0
for urun in urunler:
    toplam+=int(urun['price'])
print(toplam)

for urun in urunler:
    if int(urun['price'])<=5000:
        print(urun['name'])