start=int(input("START="))
end=int(input("end="))
for n in range(start,end+1):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        print(n)
            
