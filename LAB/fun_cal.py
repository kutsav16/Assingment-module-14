#create function for sum
def sum(num1,num2):
    return num1+num2
#create function for sub
def sub(num1,num2):
    return num1-num2
#create function for mul
def mul(num1,num2):
    return num1*num2
#create function for div
def div(num1,num2):
    return num1/num2

while True:
    print("1. Addition : ")
    print("2. subtraction :")
    print("3. mul : ")
    print("4. div : ")
    print("5. Exit :")
    # enter your choice (1-5)
    choice=int(input("Enter your choice : "))
    #enter 2 number
    num1=int(input("enter number 1 :"))
    num2=int(input("Enter number 2 :"))
    match(choice):
        case 1:
           print(sum(num1,num2))
            
        case 2:
            print(sub(num1,num2))
            
        case 3:
            print(mul(num1,num2))
            
        case 4:
            print(div(num1,num2))
            
        case 5:

            break
