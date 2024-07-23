def who_pass(dict):
    if dict:
        count=0
        for key,value in dict.items():
            #print(key,value)           
            for puan in value:
                puan=str(puan)
                new=puan.split("/")
                if new[0]==new[1]:
                    
                    count+=1
                    if count==3:
                        print(f"{key} bu dersten geçti!!")
            #print(count)
            count=0    
    return dict

dict={'cem':['15/15','5/7','8/9'],'zehra':['7/7','6/6','7/7']}
who_pass(dict)