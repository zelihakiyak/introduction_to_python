fruits={'orange','apple','banana'}
# print(fruits[0]) diyerek elemanına ulaşamayız. indekslenemez
for x in fruits:
    print(x) #sıralı şekilde vermez

fruits.add('cherry') #eleman ekleme yöntemi
fruits.update(['mango','grape']) #ekleme yöntemi ama aynı isimli elemanı eklemek istersen listenin aksine ekleme yapmaz 
print(fruits) 

fruits.remove('mango') #eleman çıkarma yöntemi
fruits.discard('apple') #elemanı çıkarma yöntemi
fruits.pop() #herhangi bir elemanı siler 
fruits.clear() #bütün elemanlar silinir.