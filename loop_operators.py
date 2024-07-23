#range
for item in range(2,10): #range(a,b,c) a=başlangıç b=sona kadar c=step sayısı
        print(item)

print(list(range(20,51,5)))  # liste şeşklinde verir.

#enumerate
greeting='hello there :)'

for index,letter in enumerate(greeting):
        print(f"index: {index} letter: {letter}")

#zip
list1=[1,2,3,4,5]
list2=['a','b','c','d','e']    
print(list(zip(list1,list2)))


for a,b in zip(list1,list2):   #for item in zip(list1,list2)
        print(a,b)                  #print(item)