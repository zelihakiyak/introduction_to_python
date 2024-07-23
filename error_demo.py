# 1:Liste elemanları içindeki sayısal değerleri bulunuz.
# lst=["1", "2", "5a", "10b", "abc", "10", "50"]
# for i in lst:
#     try:
#         res= int(i)
#         print(res)

#     except Exception:  #ValueError
#         continue

# 2:Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayısal değer 
# olduğundan emin olunuz aksi halde hata mesajı yazınız.
# while True:
#     num= input('sayi: ')
#     if num =='q':
#         break

#     try:
#         res= float(num)
#         print('girdiginiz sayi: ', res)
#     except:
#         print('geçersiz sayı')
#         continue

# 3:Girilen parola içinde türkçe karakter hatası veriniz.
# def checkPassword(psw):
#     turkce_karakter= 'ğüşİıöç'
    
#     for i in psw:
#         if i in turkce_karakter:
#             raise Exception(' Parola icinde turkce karakter mevcut.')
#         else:
#             pass

# psw= input('parola: ')

# try:
#     checkPassword(psw)
#     print('gecerli parola')
# except Exception as e:
#     print(e)

# 4:Faktöriyel fonksiyonu oluşturup 
# fonksiyona gelen değer için hata mesajları veriniz.

def fact(num):
   
    num = int(num)
    if num < 0:
        raise ValueError('Negatif deger kullanilamaz.')
    if num == 1 or num == 0:
        return 1

    else:
        return num*fact(num-1)       
    
nums=['2b',3,4,-5,'i3','5']
for n in nums:

    try:
        res= fact(n)    
        print(res)

    except Exception as e:
        print(e)
        continue

