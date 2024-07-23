"""def change(n):
    n[0]='istanbul' #kopyasının elementi değişir orijinal hali aynı kalır
    

sehirler=['ankara','izmir']


change(sehirler[:])
print(sehirler)   """ #bozulmamış liste  
# n=sehirler[:] #slicing
# print(n)  #güncellenmiş versiyonu

# def add(*params): # * --> tuple olarak alıyor
#     sum=0
#     for n in params:
#         sum+=n
#     return sum

# print(add(10,20,50))
# print(add(10,20,30))
# print(add(10,20,30,40,50,60))

# def displayUser(**args):  # ** --> dictionary olarak alıyor
#     for key, value in args.items():
#         print('{} is {}'.format(key,value))

# displayUser(name='Cinar', age=2, city= 'istanbul')
# displayUser(name='Ada', age=12, city= 'kocaeli', phone='456456')
# displayUser(name='Yigit', age=21, city= 'ankara', phone='123123', email='abc@gmail.com')

# def myfunc( a,b,*args,**kwargs):  # args-->arguments
#     print(a)                      # kwargs-->keyword arguments
#     print(b)
#     print(args)
#     print(kwargs)

# myfunc(10,20,30,40,50,key1= 'value1', key2='value2')