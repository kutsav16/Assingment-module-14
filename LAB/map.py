#Write a Python program to apply the map() function to square a list of numbers. 
#create function
def seq(num):
    return num*num
#create list
lst=[1,2,3,4,5]
#using map function
lst2=list(map(seq,lst))

print(lst2)
