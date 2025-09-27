#Write a Python program to apply the map() function to square a list of numbers. 

def seq(num):
    return num*num

lst=[1,2,3,4,5]

lst2=list(map(seq,lst))
print(lst2)