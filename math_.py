#import math as mat #1.yöntem
# value= dir(math)
# value= help(math.sqrt)
# value= math.ceil(6.7)
#value= mat.factorial(4)

from math import * #2.yöntem
#from math import sqrt,ceil,factorial

def sqrt(x):   # kütüphaneyi tanımlayan satır ile fonk tanımlanan satırdan hangisi en son okunuyorsa printte o çıkar
    print('x: '+ str(x))

value=sqrt(49) #bu yöntemde modülü belirtmeye gerek yoktur.
# value= ceil(2.3)

print(value)