# for x in range(10):
#     print(x)

numbers=[x for x in range(10)]
print(numbers)

# for x in range(10):
#     print(x**2)

numbers=[x**2 for x in range(10)]
print(numbers)

numbers=[x*x for x in range(10) if x%3==0]
print(numbers)

myString= 'hey guys'
my_list=[letter for letter in myString]
print(my_list)

years=[1983,1999,2008,1956,1986]
ages=[2019- year for year in years]
print(ages)

result=[x if x%2==0 else 'tek' for x in range(10)]
print(result)

# result=[]
# for x in range(3):
#     for y in range(3):
#         result.append((x,y))
# print(result)

numbers=[(x,y,z) for x in range (3) for y in range(3) for z in range(3)]
print(numbers)