def not_hesapla(raw):
    raw= raw[:-1]
    lst= raw.split(": ")
    studentName= lst[0]
    notes= lst[1]
    notes= notes.split(", ")
    
    not1= int(notes[0])
    not2= int(notes[1])
    not3= int(notes[2])
    avg= int((not1+ not2+ not3)/3)
   
    if avg>=85 and avg<=100:
        grade= "A"
    if avg>=70 and avg<85:
        grade= "B"
    if avg>=55 and avg<70:
        grade= "C"
    if avg>=45 and avg<55:
        grade= "D"
    if avg>=0 and avg<45:
        grade= "F"
    return studentName + ": " + grade + "\n"
def ortalamalari_oku():
    with open("nots.txt", "r", encoding="utf-8") as file:
        for raw in file:
            print(not_hesapla(raw), end="")

def not_gir():
    name=input("student name: ")
    lastname= input("student lastname: ")
    not1= input("not1: ")
    not2= input("not2: ")
    not3= input("not3: ")
    with open("nots.txt", "a", encoding="utf-8") as file:
        content= name + " " + lastname + ": " + not1 + ", " + not2+ ", " + not3 + "\n"
        file.write(content)

def notlari_kaydet():
    with open("nots.txt", "r", encoding="utf-8") as file:
        lst= []
        for i in file:
            lst.append(not_hesapla(i))
        with open("results.txt", "w", encoding="utf-8") as file1:
            for i in lst:
                file1.write(i)

while True:
    operator= input("1- Notları oku\n2- Not gir\n3- Notları kaydet\n4- Çıkış\n")
    if operator=='1':
        ortalamalari_oku()
    if operator=='2':
        not_gir()
    if operator=='3':
        notlari_kaydet()
    if operator=='4':
        break