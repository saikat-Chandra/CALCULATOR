'''
#Python Program To Build A Calculator#
print("+ Add,- Sub,* multiply,/ Divide,% rem")
num1=int(input("Enter the No 1:"))
num2=int(input("Enter the No 2:"))
operator=input ("Enter the operator:")
if operator=='+':
    print(num1+num2)
elif operator=='-':
    print(num1-num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    print(num1/num2)
elif operator=='%':
    print(num1%num2)
else:
    print("Invalid Operator")
'''
## CALCULATOR ##
'''
def add(x,y):
     add=x+y
     print("The value of addition is: ",add)
     print()
def sub(x,y):
    sub=x-y
    print("The value of substraction is: ",sub)
    print()
def mul(x,y):
    mul=x*y
    print("The value of multiplication is: ",mul)
    print()
def div(x,y):
    div=x/y
    print("The value of division is: ",div)
    print()
while(1):
    print("print 1 for add")
    print("press 2 for sub")
    print("print 3 for mul")
    print("press 4 for div")
    print()
    i=int(input("please enter your choice: "))
    if(i>=1 and i<=4):
        x1=int(input("enter the first number: "))
        y1=int(input("enter the second number: "))
        if(i==1):
            add(x1,y1)
        elif(i==2):
            sub(x1,y1)
        elif(i==3):
            mul(x1,y1)
        elif(i==4):
            div(x1,y1)
    elif(i==5):
        print("thank you")
        break
    else:
        print("wrong choice")
        print()
'''


