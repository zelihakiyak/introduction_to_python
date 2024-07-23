def linear_search(list,eleman):
    found=False
    for i in range(len(list)):
        if eleman==list[i]:
            found=True
    return found
numbers=[12,25,65,98,71]
num=int(input())
print(linear_search(numbers,num))

def merge(left,right):
    pass
