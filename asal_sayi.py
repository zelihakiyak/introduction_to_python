number=int(input("bir sayı giriniz:"))
notprime_count=0

while number>0:
    
    for x in range(2,number):
        if number%x==0:
            notprime_count+=1
        
    if notprime_count>=1 or number==1:
        print("notprime")
    else:
        print("prime")
      
    number=int(input("bir sayı giriniz:"))
    notprime_count=0
   
    