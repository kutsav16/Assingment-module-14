#Write a Python program that filters out even numbers using the filter() function. 
# create function 
def even(num):
    return num%2==0
# create list
lst=[1,2,3,4,5]

lst2=list(filter(even,lst))

print(lst2)
