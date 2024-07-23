"""def gcd(x,y):
    if y==0:
        return x
    else:
        return (gcd(x,x%y))

num1=int(input())
num2=int(input())
print(gcd(num1,num2)) """

def aye(a,b):
  if(a>b):
    kalan=a%b

    if(kalan==0):
      return b
    else:
      return aye(b,kalan)
  else:
    kalan=b%a
    
    if(kalan==0):
      return a
    else:
      return aye(a,kalan)
  
num1=int(input())
num2=int(input())
print(aye(num1,num2)) 
