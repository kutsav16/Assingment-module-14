

# create two list
lst=[1,2,3,4]
lst2=['a','b','c','d']
# create null dict
dict={}

for i in range(len(lst)):
    #lst[i] in key and lst2 in value
    dict[lst[i]]=lst2[i]
    
    

print(dict)
