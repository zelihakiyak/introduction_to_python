website= "http://www.sadikturan.com"
course= "Python Kursu: Baştan sona python programlama rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
result=len(course)
print(result)

# 2- 'website' içinden www karakterlerini alın.
result=website[7:10]  # 7den sonrakiyle başlıyor 10 dahil bitiyor.
print(result)

# 3- 'website' içinden com karakterlerini alin.
lenght=len(website)
result=website[lenght-3:lenght]
print(result)

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result=course[0:15]  # 0 yazmayabiliriz
print(result) 
result=course[-15:]
print(result)

# 5- 'course' ifadesindeki karakterleri tersten yazdırınız.
result=course[::-1] 
print(result)
result=course[::1] #düzden yazdırırr
print(result)

# 6- name, surname, age, job= 'bora', 'yılmaz', 32, 'mühendis'
# benim adım bora yılmaz , yaşım 32 ve mesleğim  mühendis
name='bora'
surname='yılmaz'
age=32
job= 'mühendis'
result= 'benim adım '+name+' '+surname+', yaşım '+str(age)+' ve mesleğim '+job
print(result)
result=f"benim adım {name} {surname}, yaşım {age} ve mesleğim {job}."
print(result)
#7 'hello world' içindeki w harfini W harfine dönüştürün
s='hello world'
s= s[:6]+ 'W'+ s[-4:]
print(s)

# 8- abc ifadesini 3 kere yazdırınız
result= 'abc '*3
print(result)
