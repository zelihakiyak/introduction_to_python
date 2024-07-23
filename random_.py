import random

# rslt= dir(random)
# rslt= help(random._random)
# rslt= random.random() #sayılar 0.0 - 1.0 arasından rastgele seçilecektir.
# rslt= random.random() * 100 
#rslt= int(random.uniform(1,100))
#rslt= random.randint(1,100)

names=['zeynep','ali','seyma','ikram','ebrar','efe','zeliha','erkim']
#rslt= names[random.randint(0,len(names)-1)] #index random atanarak yazılıyor.
# rslt= random.choice(names)

# greeting= 'hellothere'
# rslt=random.choice(greeting)

lst=list(range(100))
random.shuffle(lst) #dizi içine karışık olarak yerleştiriliyor.
rslt=random.sample(lst,4) ##ikinci argüman kadar eleman diziden seçiliyor.
rslt= random.sample(names,3)

print(rslt)