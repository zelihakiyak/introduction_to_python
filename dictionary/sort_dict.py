def to_list(dict):
    lst=[]
    if dict:
    
        dict=sorted(dict.items())
        print(dict)
        lst=list(dict)
        print(lst)
        
        
        return lst
    else:
        return lst
dict={ "b": 2, "a": 1 }
to_list(dict)   
