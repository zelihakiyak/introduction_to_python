ZelihaHesap={
    'ad':'Zeliha Kıyak ',
    'hesapNo': '1234546',
    'bakiye': 3000,
    'ekHesap':2000
}
ZahideHesap={
    'ad':'Zahide Altun',
    'hesapNo':'987654',
    'bakiye':2000,
    'ekHesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if (hesap['bakiye']>=miktar):
        hesap['bakiye']-=miktar
        print("paranızı alabilirsiniz")

    else:
        toplam=hesap['bakiye']+ hesap['ekHesap']
        if toplam>=miktar:
            ekHesapKullanımı=input("Ek  hesap kullanmak ister misiniz? (y/n)")
            if ekHesapKullanımı=='e':
                hesap['ekHesap']-=(miktar-hesap['bakiye'])
                hesap['bakiye']=0
                print("Paranızı alabilirsiniz")
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda mevcut bakiye miktarınız {hesap['bakiye']}tl ve mevcut ek hesap miktarınız {hesap['ekHesap']}tldir")
        else:
            print('Bakiyeniz yetersiniz')
            

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bakiye bulunmaktadır")


paraCek(ZelihaHesap,6000)
bakiyeSorgula(ZelihaHesap)
print("**********************")
paraCek(ZahideHesap,3000)
bakiyeSorgula(ZahideHesap)