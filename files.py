# Dosya acmak ve olusuturmak icin open() fonksiyonu kullanır.
# open(file_name, mod)

# "w": write yazma modu,
#      ** Dosyayı konumda olusturur, 
#      ** Dosya içeriğini siler ve yeniden ekleme yapar.

# file= open("newfile.txt","w")
# file.write("zeliha kiyak")
# file.close()

# "a": append ekleme, dosya konumda yoksa olusturulur

# file= open("newfile.txt","a", encoding= 'utf-8')
# file.write("\nİstanbul çok güzel bir şehir.\n")
# file.close()

# "x": create olusturma, dosya zaten varsa hata verir

#file= open("newfile2.txt", "x", encoding="utf-8")

# "r": read okuma, dosya konumda yoksa hata verir
# file= open("newfile.txt", "r", encoding="utf-8")
# for i in file:
#     print(i, end="")
# file.close()

##########
# file= open("newfile.txt", "w")
# file= open("C:/Users/ASUS/Desktop/newfile.txt", "w")
# file.close()

