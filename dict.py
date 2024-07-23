"""lst=["1=one", "2=two", "3=three", "4=four"]
def str_to_dict(lst):
    dict={}
    for i in range(len(lst)):
        new=lst[i].split("=")
        dict[new[0]]=new[1]
    return dict

print(str_to_dict(["dog=bark", "cat=meow", "cow=moo"]))
"""

def to_list(dict):
    lst=[]
    if dict:
    
        dict=sorted(dict.items())
        lst=list(dict)
        print(lst)
        
        
        return lst
    else:
        return lst
dict={ "b": 2, "a": 1 }
to_list(dict)   
