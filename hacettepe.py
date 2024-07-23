# def f(L):
#     result=[]
#     for e in L:
#         if type(e)!=list:
#             result.append(e)
#         else:
#             return f(e)
#     return result
# print (f([1,[[2,'a'],['a','b']],(3,4)]))


jan = [1, 3, 5]
feb = [3, 5, 7]
def mar(apr, may):
    if not apr or not may:
        return []
    if apr[0] == may[0]:
        return mar(apr[1:], may[1:]) + [apr[0]]
    elif apr[0] < may[0]:
        return mar(apr[1:], may)
    else:
        return mar(apr, may[1:])
    

print(mar(feb,jan))
print(len(mar(range(5, 50), range(20, 200))))
print(range(5,50))

print( mar(feb[1:], jan[1:]))