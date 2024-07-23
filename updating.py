# with open("newfile.txt", "r+", encoding= "utf-8") as file:
#     file.write("deneme")
#     #cursor sifirinci indeksde oldugu icin yazi guncellenir..
#     #file.seek(20) dersek 20.bytin oldugu yerdeki yazi guncellenir

# with open("newfile.txt", "r+", encoding= "utf-8") as file:
#     print(file.read())
    
# with open("newfile.txt", "a", encoding= "utf-8") as file:
#     file.write("\nburak kiyak")

# with open("newfile.txt", "r", encoding= "utf-8") as file:
#     print(file.read())

# ************ sayfa basinda guncelleme ********************
# with open("newfile.txt", "r+", encoding= "utf-8") as file:
#     content= file.read()
#     content= "hatice kiyak\n" + content
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# ************ sayfa ortasinda guncelleme ********************
with open("newfile.txt", "r+", encoding= "utf-8") as file:
    lst= file.readlines()
    lst.insert(1,"ali kıyak\n")
    file.seek(0)
    # for i in lst:
    #     file.write(i)
    file.writelines(lst) #ikinci yöntem for kullanmadan
with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())