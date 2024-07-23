def fib(x):
    if x<=0:
        print("lütfen sıfırdan büyük bir sayı giriniz")
    if x==1 or x==2:
        return 1
    if x>2:
        return fib(x-1)+fib(x-2)
    
x=int(input("bir sayı giriniz: "))
print(fib(x))
