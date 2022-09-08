def greatest(a,b,c):
    if((a>b)and(a>c)):
        print("GREATEST=",a)
    elif((b>a)and(b>c)):
        print("GREATEST=",b)
    else:
        print("GREATEST=",c)

a=int(input("ENTER A:"))
b=int(input("ENTER B:"))
c=int(input("ENTER C:"))
greatest(a,b,c)
