def facto(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(n,"Factorial:",fact)

def factor(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    print("Number of factors for",n,":",count)

n=int(input("N="))
if(n==0):
    print("N VALUE IS ZERO")
elif(n<0):
    print("NEGATIVE NUMBER")
else:
    facto(n)
    factor(n)

    
