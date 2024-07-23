def str_to_dict(lst):
    dict={}
    for i in range(len(lst)):
        new=lst[i].split("=")
        print(new)
        dict[new[0]]=new[1]
    return dict
#lst=["1=one", "2=two", "3=three", "4=four"]
print(str_to_dict(["dog=bark", "cat=meow", "cow=moo"]))