#faulty calci
#if you want wrong output for certain specific numbers and operators

a= input("which operator do u want to use")
b1=int(input("first number on which opearator has to be applied"))
b2=int(input("second number on which operator has to be applied"))
if(a=='*' and b1==45 and b2==3):
    print("result=555")
elif(a=='+' and b1==56 and b2==9):
    print("result=77")
elif(a=='/' and b1==56 and b2==6):
    print("result=4")
else:
    if a=='+':
        print("result=",b1+b2)
    elif a =='-':
        if b1>b2:
            print("result=",b1-b2)
        else:
            print("resullt=",b2-b1)
    elif a =='*':
        print("result=",b1*b2)
    elif a =='/':
        if b1>b2:
            print("result=",b1/b2)
        else:
            print("result=",b2/b1)
    elif a=='%':
        if b1>b2:
            print("result=",b1%b2)
        else:
            print("result=",b2%b1)
       
