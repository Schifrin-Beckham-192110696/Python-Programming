def po(x,n):
    p=pow(x,n)
    print("RESULT=",po)
def add(x,n):
    su=x+n
    print("sum=",su)
def sub(x,n):
    diff=x-n
    print("DIFFERENCE=",diff)
def mul(x,n):
    m=x*n
    print("PRODUCT=",m)    
def div(x,n):
    qu=x/n
    print("QUOTIENT=",qu)

x=int(input("ENTER X VALUE:"))
n=int(input("ENTER N VALUE:"))
c=int(input("ENTER THE CHOICE:"))

if c==1:
    po(x,n)
elif c==2:
    add(x,n)
elif c==3:
    sub(x,n)
elif c==4:
    mul(x,n)
elif c==5:
    try:
      div(x,n)
    except ZeroDivisionError:
        print("DENOMINATOR CANNOT BE ZERO")
else:
    print("INVALID")





    
