# with yöntemiyle scope içerisinde istediklerimizi yaptırırız.
# close() fonksiyonunu kullanmamıza gerek yoktur.

with open("newfile.txt", "r", encoding= "utf-8") as file:
    content= file.read(5)
    print(content)
    file.seek(0)            # cursor girilen satır numarasına gider
    print(file.tell())      # o anda cursorun hangi satır olduğunu söyler.
    content2= file.read(10) # girilen size byteı kadar okur.
    print(content2)