#Write a generator function that generates the first 10 even numbers. 

def Even():
    num=2
    count=0
    while count<10:
        yield num
        num +=2
        count +=1
        
for i in Even():
    print(i)