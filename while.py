# x=0
# while x<=100:
#     if x%2==0:
#         print(f"{x} sayısı bir çift sayıdır.")
#     else:
#         print(f"{x} sayısı bir tek sayıdır.")
#     x+=1

name='' #false
while not name.strip():
    name=input("isminizi giriniz: ")
print(f"merhaba {name}")