

for rakam in range(2):
    x=int(input())
    counter=0
    while x!=1:
        if x%2==0:
            x=x/2
            counter+=1
        else:
            x=(x*3)+1
            counter+=1
    print(counter)    

