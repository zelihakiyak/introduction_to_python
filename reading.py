# try:
#     f= open("newfile1.txt", "r")
#     print(f)
#     print("dosya kapandı")
#     f.close()
    
# except FileNotFoundError:
#     print("okuma hatası")

file= open("newfile.txt", "r", encoding= "utf-8")
# #for döngüsüyle
# for i in file:
#     print(i, end="")

# #read fonksiyonuyla
# content1= file.read()
# print("icerik 1")
# print(content1)

# file= open("newfile.txt", "r", encoding= "utf-8")
# content2= file.read()
# print("icerik 2")
# print(content2)
# file.close()

# content= file.read(5)
# content= file.read(7)
# print(content)

# readline() fonksiyonuyla
# file= open("newfile.txt", "r", encoding= "utf-8")
# print(file.readline(), end="")
# print(file.readline(), end="")

# readlines() fonksiyonuyla
file= open("newfile.txt", "r", encoding= "utf-8")
liste= file.readlines()
print(liste)
file.close()