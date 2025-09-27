#Write a Python program that uses a custom iterator to iterate over a list of integers. 

def iterate(num):
    for i in num:
        yield i
        
lst=[10,20,30,40,50]
for i in iterate(lst):
    print(i)
    
    
lst=[10,20,30,40,50]   
it=iter(lst)


num= next(it)
print(num)