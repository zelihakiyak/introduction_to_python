# key-value
# 41--> Kocaeli  34--> İstanbul

sehirler=['kocaeli','istanbul']
plakalar=[41,34]

print(plakalar[sehirler.index('istanbul')])

plakalar= {'kocaeli':41, 'istanbul':34}
print(plakalar['kocaeli'])
print(plakalar['istanbul'])

plakalar['ankara']=6  #listeye ekleme yapar
print(plakalar)

users={
    'zelihakiyak': {
        'age':20,
        'rıles':['admin','user'],
        'email':'zelihakyk64.43@hotmail.com',
        'adres':'uşak',
        'tel':5511222418
    },
    'zahidealtun': {
        'age':20,
        'rıles':['user'],
        'email':'..@gmail.com',
        'adres':'antalya',
        'tel':123123

    },
    'ruveydaisözen':21,
    'figentsc':22
}
print(users['zelihakiyak']['age'])
print(users['zelihakiyak']['email'])
print(users['zelihakiyak']['email'])
print(users['zelihakiyak']['adres'])
print(users['zelihakiyak']['tel'])
