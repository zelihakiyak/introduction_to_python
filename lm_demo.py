names=['Ali','Yağmur','Hakan','Deniz']
years=[1998,2000,1998,1987]

# names.append('Cenk') #ismi listenin sonuna ekle
# print(names)
# names.insert(0,'Sena') #ismi listenin başına ekle
# print(names)
# names.remove('Deniz') #ismi listeden sil
# print(names)
# index=names.index('Yağmur') #ismin indeksini verir
# names.pop(index) #indeksi bilinmeyen elemanı bulduktan sonra siler
# print(names)
# result=names.count('Mehmet') #isim listeden var mı kontrol eder
# #result= 'Ali' in names
# #result=name.index('Ali')
# print(result)
# result=names[::-1] #elemanları sağdan sola yani tersten yazdırır
# print(result)
# names.sort() #alfabetik olarak sıralar
# print(names)

# str="chevrolet,dacia" #karakter dizisini listeye çevirir
# result=str.split(',')
# print(result  )

# mini=min(years) #dizinin max ve min değerini bulur
# maxi=max(years)
# print(mini,maxi)

# result=years.count(1998) #kaç tane olduğunu verir
# print(result)

# years.clear() #listenin elemanlarını siler
# print(years)

# markalar=[]
# i=0
# while i<3:
#     marka=input()
#     i+=1
#     markalar.append(marka)

# print(markalar)
# years.remove(1987)
# print(years)

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname,self.age)

# class Student(Person):
#   def __init__(self, fname, lname,age):
#     super().__init__(fname, lname)
#     self.age=age




class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print ("Welcome", self.firstname,"?", self.lastname, "to the class of", self.graduationyear)
  def __str__(self):
    return f'welcome {self.firstname} ? {self.lastname} to the class of {self.graduationyear}'

s1=Student("zeliha","kıyak",2003)
s2=Student("şeyma","kula",2004)
print(s1)
print(s2)