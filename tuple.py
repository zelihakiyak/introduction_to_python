list=[1,2,3]
tuple=(1,'iki',3,8,1) #tuple= 1,'iki',3,8,1 de yazılabilir

print(tuple[2])
print(len(tuple))
list[0]= 'ahmet' #tuple[0]='deniz' diyerek atama işlemi yapamayız!!


tuple=('ayşe','damla','zehra','damla')
names=('zeliha','zahide','rüveyda','figen') + tuple
print(names)

print(tuple.count('damla'))
print(tuple.index('zehra'))