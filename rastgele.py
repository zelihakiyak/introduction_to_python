import random
number_of_rolls=2
sıklık1=0
sıklık2=0
sıklık3=0
sıklık4=0
sıklık5=0
sıklık6=0

for roll in range(number_of_rolls):
    face=random.randrange(1,7)
    if face==1:
        sıklık1+=1
    elif face==2:
        sıklık1+=1
    elif face==3:
        sıklık1+=1
    elif face==4:
        sıklık1+=1
    elif face==5:
        sıklık1+=1
    elif face==6:
        sıklık1+=1
    print(sıklık1)
    print(sıklık2)
    print(sıklık3)
    print(sıklık4)
    print(sıklık5)
    print(sıklık6)
    

x=123.456789
print("%.2f"%x)

print("{:.2f}".format(x))

print(f"{x:.2f}")
print(f"{x}:.2f")
