#simple calculator 
i=0
while i==0:

    x=int(input("enter the numbers "))
    y=int(input("enter the second number "))


    print("if you want to do addition please enter 1")
    print("if you want to do subtraction please enter 2")
    print("if you want to do multiplication please enter 3")
    print("if you want to do division please enter 4")
    print("if you want to calculate reminder please enter 5")


    a=int(input("enter the number according to your requirement "))


    if(a==1 ):
            print("addition is" ,x+y)
    elif(a==2):
        print("subtraction is",x-y)
    elif(a==3):
        print("multiplication is",x*y)
    elif(a==4):
        print("division is ",x/y) 
    elif(a==5):
        print("calculated reminder is ",x%y)
    else:
        print("invalid input please try again")            



        i +=1