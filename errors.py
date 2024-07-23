#some error types
# print(a) # Name error
# print('1a2') # Value error
# print(10/0) # Zero division error
# print('denem'e) #Syntax error

# error handling
while True:
    try: 
        x= int(input('x: '))
        y= int(input('y: '))
        print(x/y)
    except Exception as ex:
    #except (ZeroDivisionError, ValueError) as e:
        print('gecersiz bir bilgi girdiniz', ex)
      
    else:      # else bloğu try bloğu çalışırsa ve except bloğu çalışmazsa aktif olur
        print('her sey yolunda')
        break
    finally:   # try ya da except çalışsın fark etmez her zaman çaşışır.
        print('try except sonlandi.')