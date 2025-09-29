#Write a generator function that generates the first 10 even numbers. 
#create function for generater
def Even():
    #starting num value from 2
    num=2
    count=0
    while count<10:
        yield num
        #num value num+=2
        num +=2
        #count++
        count +=1
        
for i in Even():

    print(i)
