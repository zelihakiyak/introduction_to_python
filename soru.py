#alınan değerleri tek ve çift ayrı ayrı toplamlarını yazdıran kod


tektotal=0
cifttotal=0
for sayi in range(5):
    x=int(input())

    if ((x%2)==0):
        cifttotal=cifttotal+x

    else:
        tektotal=tektotal+x



print("çift sayıların toplamı:",cifttotal)
print("tek sayıların toplamı",tektotal)


