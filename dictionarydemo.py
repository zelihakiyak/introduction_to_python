students={}
i=1
while i<3:
    numbers=input("öğrenci nonuzu girin:")
    names=input("adınızı girin:")
    surnames=input("soyadınızı girin:")
    phones=input("telefon nonuzu girin:")
    
    students.update({
        numbers: {
            'ad': names,
            'soyad':surnames,
            'tel': phones
        }         
    })
    i+=1

print(students)

print('*'*50)

studentsnumber=input('öğrenci no:')
student=students[studentsnumber]
print(f" Aradığınız {studentsnumber} nolu öğrencinin adı:{student['ad']} soyadı:{student['soyad']} ve telefonuysa {student['tel']}")